from django.views.generic import ListView, DetailView
from assessment.models import Interface_project, Post ,Interface
from account.models import User


# ListView
class PostLV(ListView):
    model = Post
    template_name = 'assessment/post_all.html' # 템플릿 파일명 변경
    context_object_name = 'posts' # 컨텍스트 객체 이름 변경(object_list)
#  paginate_by = 6 # 페이지네이션, 페이지당 문서 건 수    
    def get_context_data(self, **kwargs) :
        context= super().get_context_data(**kwargs)
        context['object_list']=Interface.objects.all()
        return context



    def get_context_data_pro(self, **kwargs) :
        context= super().get_context_data(**kwargs)
        context['object_list']=Interface_project.objects.all()
        return context

#  class InstrouctionDV(DetailView):
#     model = Instrouction
#     ## defatul : templates/app_name/model_detail
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs) # object 만들어낸다.
#         context['object_list'] = Instrouction.objects.all()
#         return context


# DetailView
class PostDV(DetailView):
    model = Post

