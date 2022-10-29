from django.urls import path 

from .import directorviews
from .import employeeviews
urlpatterns = [
    path('hrm/',directorviews.director,name='directors'),
    path('employee/',employeeviews.staff,name='employee'),
    path('todo/add/',employeeviews.addTodo,name='todo'),
    path('todo/pending/',employeeviews.pendingtodo,name='pending'),
    path('todo/complete/',employeeviews.completetodo,name='complete'),
    path('todo/<int:is_completed>/completed/',employeeviews.is_completed,name='is_completed'),
    path('todo/delete/complete/all/',employeeviews.deleteComplete,name='deletecomplete'),
    path('todo/delete/all/',employeeviews.alldelete,name='alldelete'),
]

