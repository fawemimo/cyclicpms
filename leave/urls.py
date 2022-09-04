from django.urls import path

# from managements import employeeviews
from managements.employee import my_leave

urlpatterns = [
    path('',my_leave.employee_apply_leave_save,name='leave')
]