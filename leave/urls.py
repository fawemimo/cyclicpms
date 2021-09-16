from django.urls import  path

from managements import employeeviews


urlpatterns = [
    path('',employeeviews.employee_apply_leave_save,name='leave')
]