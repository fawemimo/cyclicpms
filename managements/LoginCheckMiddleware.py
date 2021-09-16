from django.http import HttpResponseRedirect
from django.shortcuts import reverse,redirect, render 
from django.utils.deprecation import MiddlewareMixin
from managements.directorviews import *
from accounts.models import User

class LoginCheckMiddleware(MiddlewareMixin):
    def process_view(self,request,view_func,view_args,view_kwargs):
        modulename = view_func.__module__
        user = request.user
        if user.is_authenticated:
            if user.user_type == 5:
                
                if modulename == 'managements.directorviews':
                    pass
                elif modulename == 'accounts.views':
                    pass
                else:
                    return redirect('error_page')
                
            if user.user_type == 1:
                
                if modulename == 'managements.employeeviews':
                    pass
                elif modulename == 'accounts.views':
                    pass
                else:
                    return redirect('error_page')    
                    
        else:
            if request.path == reverse('accounts-login') or request.path == reverse('home')      :
                pass
            else:
                return redirect('accounts-login')