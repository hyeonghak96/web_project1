from django.urls import path
from instrouction.views import InstrouctionLV, InstrouctionDV

app_name ='instrouction'

urlpatterns = [
    path('', InstrouctionLV.as_view(), name='index'),
    path('<int:pk>/', InstrouctionDV.as_view(), name='detail'),


]