# from accounts.models import Profile
from django.http import HttpResponse
from django.shortcuts import render

from managements.models import Employee


# Create your views here.
def staff(request):
    if not request.user.user_type == 1:
        return HttpResponse('You are not allow to view this page')   
    else:
        # profile                 = Profile.objects.get(user=request.user.id)
        employee        = Employee.objects.get(user=request.user.id)
        context = {
            'employee':employee
        }
        
    return render(request,'dashboards/employee_template/employee.html',context)