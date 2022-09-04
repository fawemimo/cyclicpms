from django.urls import path

from . import views

urlpatterns = [
    path('',views.index,name='home'),
    # path('payroll-manager/', views.payroll_upload, name='payroll_upload' ),
]
