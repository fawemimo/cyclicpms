from django.urls import path,include
from .views import *
from rest_framework.routers import DefaultRouter


routers = DefaultRouter()
post_router=routers.register('post', PostList, basename='post')

urlpatterns = [
    # path('',include(routers.urls)),
    path('',PostList.as_view(), name='listcreate'),
    path('<int:pk>/',PostDetail.as_view(), name='listdetail'),
    path('user/register/', CustomUserAPI.as_view()),
    path('logout/backlist/', BlacklistTokenView.as_view(),name='blacklist'),
    path('search/',PostListDetailFilter.as_view()),

    # Admin urks
    path('admin/create/',CreatePost.as_view(),name='createpost'),
    path('admin/edit/postdetail/<int:pk>/', AdminPostDetail.as_view()),
    path('admin/delete/<int:pk>/', DeletePost.as_view()),
]