from typing import List
from django.shortcuts import render

# Create your views here.

from django.views.generic import ListView, DetailView
from instrouction.models import Instrouction


class InstrouctionLV(ListView):
    model = Instrouction

class InstrouctionDV(DetailView):
    model = Instrouction
    ## defatul : templates/app_name/model_detail
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) # object 만들어낸다.
        context['object_list'] = Instrouction.objects.all()
        return context


# from django.views.generic import CreateView, UpdateView, DeleteView
# from django.contrib.auth.mixins import LoginRequiredMixin
# from django.urls import reverse_lazy
# from mysite.views import OwnerOnlyMixin

# class InstrouctionCreateView(LoginRequiredMixin,CreateView):
#     model = Instrouction
#     fields =['title','contenthead','content'] #생성할 목록들
#     success_url = reverse_lazy('instrouction:index') #완료되면 돌아갈 페이지

#     def form_valid(self,form):   # 타당성 검사
#         form.instance.owner = self.request.user # owner가 user에 있다면
#         return super().form_valid(form)   #조상쪽 가서 타당성 확인해라

# class InstrouctionChangeLV(LoginRequiredMixin,ListView):
#     template_name = 'instrouction/instrouction_change_list.html' #여기서 바꿀거임
#     def get_queryset(self): #쿼리셋 함수를 만들껀데
#         return Instrouction.objects.filter(owner =self.request.user) #로그인한 사용자


# class InstrouctionUpdateView(OwnerOnlyMixin,UpdateView):
#     model = Instrouction
#     field = ['title','contenthead','content']
#     success_url = reverse_lazy('indstrouction:index')

# class InstrouctionDeleteView(OwnerOnlyMixin, DeleteView):
#     model = Instrouction
#     success_url = reverse_lazy('instrouction:index')
