from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView, FormView, CreateView, UpdateView, DeleteView
from django.db.models import Q, F
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from mysite.views import OwnerOnlyMixin
from django.http import FileResponse
from blog.forms import PostSearchForm
import os
from django.conf import settings
from .models import Board, BoardAttachFile, Album, Photo
# Create your views here.

# ListView
class BoardLV(ListView):
    model = Board
    template_name = 'board/post_all.html'   # 템플릿 파일명 변경
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
    template_name = 'blog/post_search.html'

    def form_valid(self, form):
        searchWord = form.cleaned_data['search_word']
        post_list = Board.objects.filter(
            Q(title__icontains=searchWord) |
            Q(description__icontains=searchWord) |
            Q(content__icontains=searchWord)
        ).distinct()

        context = {}
        context['form'] = form
        context['search_term'] = searchWord
        context['object_list'] = post_list

        return render(self.request, self.template_name, context)

class BoardCreateView(LoginRequiredMixin, CreateView):
    model = Board
    fields = ['title', 'slug', 'description', 'content', 'tags']
    initial = {'slug': 'auto-filling-do-not-input'}
    success_url = reverse_lazy('blog:index')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        # return HttpResponseRedirect(self.get_success_url())
        response = super().form_valid(form)  # Post 모델 저장, self.object

        # 업로드 파일 얻기
        files = self.request.FILES.getlist("files")
        for file in files:
            attach_file = BoardAttachFile(post=self.object, filename = file.name,
                                        size = file.size, content_type = file.content_type,
                                        upload_file = file)
            attach_file.save()

        return response

        # return super().form_valid(form)

class BoardUpdateView(OwnerOnlyMixin, UpdateView):
    model = Board
    fields = ['title', 'description', 'content', 'tags']
    success_url = reverse_lazy('board:index')

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
            attach_file = BoardAttachFile(post=self.object,filename = file.name,
            size = file.size, content_type = file.content_type, upload_file = file)
            attach_file.save()
        return response

class BoardDeleteView(OwnerOnlyMixin, DeleteView):
    model = Board
    success_url = reverse_lazy('blog:index')


def download(request, id):
    file = BoardAttachFile.objects.get(id=id)
    file_path = os.path.join(settings.MEDIA_ROOT, str(file.upload_file))

    return FileResponse(open(file_path, 'rb'))


# 자세히보기 뷰(https://nachwon.github.io/django-12-post-detail/)
def board_detail(request):
    board = Board.objects.first()
    context = {
        'board': board
    } 
    return render(request, 'board/board_detail.html', context)

class AlbumLV(ListView):
    model = Album

class AlbumDV(DetailView):
    model = Album

class PhotoDV(DetailView):
    model = Photo

    