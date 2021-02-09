from django.urls import path
from instrouction.views import InstrouctionLV, InstrouctionDV

app_name ='instrouction'

urlpatterns = [
    path('', InstrouctionLV.as_view(), name='index'), #index는 들어가는걸 담당한다.
    path('list/', InstrouctionDV.as_view(), name ='list'),
    path('list/intro', InstrouctionDV.as_view(), name ='intro'),
    path('list/structure', InstrouctionDV.as_view(), name ='structure'),
    path('list/plan', InstrouctionDV.as_view(), name ='plan'),


]