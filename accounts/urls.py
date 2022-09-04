from django.urls import path
from .import views
# from accounts.views import LoginView

urlpatterns = [
    
    path('login/',views.login_page,name='accounts-login'), 
    path('logout/',views.logout,name='accounts-logout'),
    path('verify/',views.verify_view,name='accounts-verify'), 
    # path('profile/',views.profile,name='accounts-profile'),
    
]