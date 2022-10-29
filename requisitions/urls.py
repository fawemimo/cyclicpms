from django.urls import path
from .import views


urlpatterns   = [
    path('apply/',views.req_apply,name="req_apply")
]