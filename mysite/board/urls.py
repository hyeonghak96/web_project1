from mysite.board.views import AlbumDV, AlbumLV, PhotoDV
from django.urls import path, re_path
from django.urls.resolvers import path, re_path
from blog.views import *

app_name = 'board'

urlpatterns = [
    path('', BoardLV.as_view(), name='index'),
    path('<int:pk>/', BoardDV.as_view(), name='detail'),
    path('tag/', TagCouldTV.as_view(), name='tag_cloud'),
    path('tag/<str:tag>/', TaggedObjectLV.as_view(), name='tagged_object_list'),
    path('search/', SearchFormView.as_view(), name='search'),
    path('add/', BoardCreateView.as_view(), name='add'),
    path('<int:pk>/update/', BoardUpdateView.as_view(), name='update'),
    path('<int:pk>/delete', BoardDeleteView.as_view(), name='delete'),
    path('download/<int:id>', download, name='download'),
    path('', AlbumLV.as_view(), name='photo_index'),
    path('album', AlbumLV.as_view(), name='album_list'),
    path('album/<int:pk>/', AlbumDV.as_view(), name='album_detail'),
    path('photo/<int:oj>/', PhotoDV.as_view(), name='photo_detail'),
]