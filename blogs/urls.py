from os import name

from django.urls import path

from . import views
from .views import (PostCreateView, PostDeleteView,  # PostListView,
                    PostDetailView, PostUpdateView, UserPostListView)

urlpatterns  = [
    # path('', PostListView.as_view(),name='bloghome'),
    path('',views.postlist,name='bloghome'),
    path('user/<str:username>', UserPostListView.as_view(),name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(),name='post-detail'),
    path('post/new/', PostCreateView.as_view(),name='post-create'),    
    path('post/<int:pk>/delete/', PostDeleteView.as_view(),name='post-delete'),      
    path('post/<int:pk>/update/',views.post_update,name='post_update'),
]