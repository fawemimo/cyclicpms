from django.urls import path

from . import views
from .employee.views import payslip_data
from .hrm.views import *

urlpatterns = [
    path('',views.index,name='home'),
    path('payslip/',payslip_data,name='payslip'),
    # path('payroll-manager/', views.payroll_upload, name='payroll_upload' ),
    path('jobrole/add/',jobrole_page,name='jobrole_page'),
    path('jobrole/add/save/',job_role_save,name='job_role_save')
]
