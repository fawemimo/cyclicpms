from django.urls import path

# from  .views import PersonalView
from . import views

urlpatterns = [
    path('',views.personalinfo,name='personalinfo'),
    path('bank/',views.bankdetail,name='bankdetail'),
    path('education/',views.education,name='education'),
    # path for file upload     
    path('file_upload/',views.file_upload,name='file_upload'),
    path('file_upload_save/',views.file_upload_save,name='file_upload_save'),
    # path for success page on for submission 
    path('success_page/',views.success_page,name='success_page')
]
