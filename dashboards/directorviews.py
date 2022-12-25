from http.client import HTTPResponse
from django.shortcuts import render

# Create your views here.
from blogs.models import Post
from directors.models import Director
from managements.models import Employee
# from accounts.models import Profile,User

def director(request):
    if request.user.user_type != 5:
        return HTTPResponse('You are not allow to view this page')
        
    return render(request,'dashboards/director_template/director.html')