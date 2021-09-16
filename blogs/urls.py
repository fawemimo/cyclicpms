from os import name
from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView,
    
    
    
)
from . import views

urlpatterns  = [
    path('', PostListView.as_view(),name='bloghome'),
    path('user/<str:username>', UserPostListView.as_view(),name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(),name='post-detail'),
    path('post/new/', PostCreateView.as_view(),name='post-create'),
    # path('post/new/',views.post_create_view,name='post-create'),
    # path('post/<int:pk>/update/', PostUpdateView.as_view(),name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(),name='post-delete'),
    
    
    # path('post/new/',views.post_create_view,name='post_create_view'),
    path('post/<int:pk>/update/',views.post_update,name='post_update'),
]