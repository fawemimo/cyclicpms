from django.urls import path
from .import views
# from accounts.views import LoginView
from .hrm.corporate_signup import account_register,account_activate

urlpatterns = [
    
    path('login/',views.login_page,name='accounts-login'), 
    path('logout/',views.logout,name='accounts-logout'),
    path('verify/',views.verify_view,name='accounts-verify'), 
    # path('profile/',views.profile,name='accounts-profile'),
    path('hrm/join/',account_register,name='join'),
    path('activate/<uidb64>/<token>/',account_activate, name='accounts-activate'),
    
]