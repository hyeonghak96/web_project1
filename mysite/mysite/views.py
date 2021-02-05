from django.views.generic import TemplateView, ListView, DetailView

# TemplateView
class HomeView(TemplateView):
    template_name = 'home.html'

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
        