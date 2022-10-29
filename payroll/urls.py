from django.urls import path

from . import views
from .employee.views import payslip_data

urlpatterns = [
    path('',views.index,name='home'),
    path('payslip/',payslip_data,name='payslip'),
    # path('payroll-manager/', views.payroll_upload, name='payroll_upload' ),
]
