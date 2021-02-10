from django.views.generic import TemplateView ,CreateView
# from django.contrib.auth.forms import UserCreationForm
from account.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView
from blog.models import Post
from django.core.paginator import Paginator


# TemplateView
class HomeView(ListView):
    template_name = 'home.html'
    
    model = Post
    paginate_by = 5
    def get_context_data(self,**kwargs):  
        context = super().get_context_data(**kwargs)
        # context['object_list'] = Post.objects.all()
        return context

    

#--- User Creation
class UserCreateView(CreateView): 
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('register_done')


class UserCreateDoneTV(TemplateView): 
    template_name = 'registration/register_done.html' 
class InstrouctionView(TemplateView):
    template_name = 'instrouctionbase.html'

class InstrouctionIntroView(TemplateView):
    template_name = 'instrouction_intro.html'

class InstrouctionStructureView(TemplateView):
    template_name = 'instrouction_structure.html'

class InstrouctionPlanView(TemplateView):
    template_name = 'instrouction_plan.html'


from django.contrib.auth.mixins import AccessMixin
from django.views.defaults import permission_denied


class OwnerOnlyMixin(AccessMixin):
    raise_exception = True
    permission_denied_message = " Owner only can update/delete the object"

    def get(self,request, *args, **kwargs):
        self.object = self.get_object() # 모델인스턴스# 내용 리스트담김
        if self.request.user != self.object.owner:  # 소유자가 아니라면
            self.handle_no_permission() # 예외발생

        return super().get(request,*args,**kwargs)
        
