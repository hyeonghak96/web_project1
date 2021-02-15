from django.views.generic import TemplateView ,CreateView
# from django.contrib.auth.forms import UserCreationForm
from account.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView
from blog.models import Post
from django.core.paginator import Paginator

import calendar
from calendar import HTMLCalendar
from datetime import datetime
from django.shortcuts import render


# TemplateView
class HomeView(ListView):
    template_name = 'home.html'
    
    model = Post
    paginate_by = 5
    def get_context_data(self,**kwargs):  
        context = super().get_context_data(**kwargs)
        # context['object_list'] = Post.objects.all()

        year=datetime.now().year
        month=datetime.now().strftime('%B')
        month = month.capitalize()
        # Convert month from name to number
        month_number = list(calendar.month_name).index(month)
        month_number = int(month_number)

        # create a calendar
        cal = HTMLCalendar().formatmonth(
            year,
            month_number)
        # Get current year
        now =datetime.now()
        current_year = now.year

        # Get current time
        time =now.strftime('%I:%M:%S %p')  
        # context["year"]  = year

        context.update({
            "year":year,
            "month":month,
            "month_number":month_number,
            "cal": cal,
            "current_year":current_year,
            "time":time,
            })

        return context
    

    

#--- User Creation
class UserCreateView(CreateView): 
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('register_done')

class ProfileView(TemplateView):
    template_name = 'registration/profile.html'    


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







from django.shortcuts import render

import calendar
from calendar import HTMLCalendar
from datetime import datetime



        
