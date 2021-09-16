from django.shortcuts import render

# Create your views here.
def staff(request):
    return render(request,'dashboards/employee_template/employee.html')