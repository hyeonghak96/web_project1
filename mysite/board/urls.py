from django.urls import path, re_path
from .views import *



app_name = 'board'

urlpatterns = [
    path('', BoardLV.as_view(), name='index'),
    path('<int:pk>/', BoardDV.as_view(), name='detail'),
    path('tag/', TagCloudTV.as_view(), name='tag_cloud'),
    path('tag/<str:tag>/', TaggedObjectLV.as_view(), name='tagged_object_list'),
    path('search/', SearchFormView.as_view(), name='search'),
    path('add/', BoardCreateView.as_view(), name='add'),
    path('<int:pk>/update/', BoardUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', BoardDeleteView.as_view(), name='delete'),
    path('download/<int:id>', download, name='download'),
    path('comment/<int:id>', BoardDV.as_view(), name="comment"),

    # path('comment/create/question/<int:board_id>/', views.comment_create_question, name='comment_create_question'),
    # path('comment/modify/question/<int:comment_id>/', views.comment_modify_question, name='comment_modify_question'),
    # path('comment/delete/question/<int:comment_id>/', views.comment_delete_question, name='comment_delete_question'),
] 