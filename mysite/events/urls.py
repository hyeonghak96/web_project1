from django.urls import path, re_path
from events import views
from events.views import *



app_name = 'events'
urlpatterns = [
    # Path Converters
    # int: numbers
    # str: strings
    # path: whole urls/
    # slug: hyphen-and_underscores_stuff


    # path('',EventLV.as_view(), name="index"),
    path('',EventLV.as_view(),name='home'),
    path('<int:year>/<str:month>/',EventLV.as_view())
   
]
