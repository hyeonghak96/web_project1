from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, DetailView, TemplateView, FormView, CreateView, UpdateView, DeleteView
from django.db.models import Q, F
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from mysite.views import OwnerOnlyMixin
from django.http import FileResponse
from .forms import BoardSearchForm # , CommentForm
import os
from django.conf import settings
from .models import Board, BoardAttachFile
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

# Create your views here.

# ListView
class BoardLV(ListView):
    model = Board
    template_name = 'board/board_index.html'   # 템플릿 파일명 변경
    context_object_name = 'boards'          # 컨텍스트 객체 이름 변경(object_list)
    paginate_by = 10                        # 페이지네이션, 페이지 당 문서 건 수

# DetailView
class BoardDV(DetailView):
    model = Board

#--- Tag View
class TagCloudTV(TemplateView):
    template_name = 'taggit/taggit_cloud.html'

class TaggedObjectLV(ListView):
    template_name = 'taggit/taggit_post_list.html'
    model = Board

    def get_queryset(self):
        return Board.objects.filter(tags__name=self.kwargs.get('tag'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tagname'] = self.kwargs['tag']
        return context

#--- FormView
class SearchFormView(FormView):
    form_class = BoardSearchForm
    template_name = 'board/board_search.html'

    def form_valid(self, form):
        searchWord = form.cleaned_data['search_word']
        board_list = Board.objects.filter(
            Q(title__icontains=searchWord) |
            Q(description__icontains=searchWord) |
            Q(content__icontains=searchWord)
        ).distinct()

        context = {}
        context['form'] = form
        context['search_term'] = searchWord
        context['object_list'] = board_list

        return render(self.request, self.template_name, context)

class BoardCreateView(LoginRequiredMixin, CreateView):
    model = Board
    fields = ['title', 'description', 'content', 'tags']
    success_url = reverse_lazy('board:index')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        # return HttpResponseRedirect(self.get_success_url())
        response = super().form_valid(form)  # Post 모델 저장, self.object

        # 업로드 파일 얻기
        files = self.request.FILES.getlist("files")
        for file in files:
            attach_file = BoardAttachFile(board=self.object, filename = file.name,
                                        size = file.size, content_type = file.content_type,
                                        upload_file = file)
            attach_file.save()

        return response

        # return super().form_valid(form)

class BoardUpdateView(OwnerOnlyMixin, UpdateView):
    model = Board
    fields = ['title', 'description', 'content', 'tags']
    success_url = reverse_lazy('board_index.html')

    def form_valid(self, form):
        delete_files = self.request.POST.getlist("delete_files")
        for fid in delete_files:
            file = BoardAttachFile.objects.get(id=int(fid))
            file_path = os.path.join(settings.MEDIA_ROOT, str(file.upload_file))
            os.remove(file_path)
            file.delete()
            
        response = super().form_valid(form)

        files = self.request.FILES.getlist("files")
        for file in files:
            attach_file = BoardAttachFile(board=self.object,filename = file.name,
            size = file.size, content_type = file.content_type, upload_file = file)
            attach_file.save()
        return response

class BoardDeleteView(OwnerOnlyMixin, DeleteView):
    model = Board
    success_url = reverse_lazy('board_index.html')

# class CommentCreateView:
    
#     def comment(request, board_id):

#         if request.method == "BOARD":
#             comment_form = CommentForm(request.BOARD)
#             comment_form.instance.author_id = request.user.id
#             comment_form.instance.board_id = board_id
#             if comment_form.is_valid():
#                 comment = comment_form.save()

#         return HttpResponseRedirect(reverse_lazy('board:detail', args=[board_id]))



def download(request, id):
    file = BoardAttachFile.objects.get(id=id)
    file_path = os.path.join(settings.MEDIA_ROOT, str(file.upload_file))

    return FileResponse(open(file_path, 'rb'))


def view(request, no=0, page=1):
    # 존재하는 게시글이 없을 경우 return
    if no == 0:
        return HttpResponseRedirect('list')

    board = Board.objects.filter(id=no)

    data = {
        'board':board[0],
        'page':page,
    }

    response = render(request, 'board/board_detail.html', data)
    if request.session.get('authUser') is None:
        cookie_name = 'hit'
    else:
        cookie_name = f'hit:{request.session["authUser"]["id"]}'


    if request.COOKIES.get(cookie_name) is not None:
        cookies = request.COOKIES.get(cookie_name)
        cookies_list = cookies.split('|')
        if str(no) not in cookies_list:
            board.update(hit=F('hit') + 1)
            return response
    else:
        board.update(hit=F('hit') + 1)
        return response

    return render(request, 'board/board_detail.html', data)



