from django.urls import path,include
from .views import *
from rest_framework import routers

routers= routers.SimpleRouter()
routers.register('user', UserViewSet, basename='user')

urlpatterns = [
    path('',include(routers.urls)),
    path('functions/',all_user_view),
    path('functions/<int:id>',single_user_details_view),
    path('userapiview/',UserAPIView.as_view()),
    path('userapiview/<int:id>/',UserDetailAPIView.as_view()),
    path('usergenericviews/',UserGenericView.as_view()),
    path('usergenericviews/<int:id>/',UserGenericView.as_view()),
    path('login/',LoginView.as_view()),
    path('logout/',LogoutAPIView.as_view()),
    path('usefilter/',UserFilterListView.as_view({'get':'pk'})),
    path('upload/',UploadView.as_view(),name='file_upload')
]