from django.urls import path
from .import views

urlpatterns = [
    path('',views.contact,name='contacts'),
    path('subscribe/',views.subscribers,name='contacts-letter'),
    path('unsubscribe/',views.unsubscribe,name='contacts-unsubcribe'),
    path('mail/',views.mail_letter,name='contacts-mail'),
    
]