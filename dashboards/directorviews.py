from django.shortcuts import render

# Create your views here.
from blogs.models import Post
from directors.models import Director
from managements.models import Employee
# from accounts.models import Profile,User

def director(request):
    director = Director.objects.annotate('company')
    employee = Employee.objects.all().filter(director=director)
    print(director)
    return render(request,'dashboards/director_template/director.html')