from django.urls import path 

from .import directorviews
from .import employeeviews
urlpatterns = [
    path('director/',directorviews.director,name='directors'),
    path('employee/',employeeviews.staff,name='employee'),
]