from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from blogs.models import Post
from category.models import *
from directors.models import *
from leave.models import LeaveReportEmployee


def director_context(request):
    directors = Director.objects.get(user=request.user.id)
    categories = AddCategory.objects.all()
    blogs = Post.objects.all().order_by('-date_posted')[:5]
    director = get_object_or_404(Director, user=request.user.id)
    employee = Employee.objects.all().filter(director=director).count()
    leaveemployee = LeaveReportEmployee.objects.filter(leave_status=0).count()    
    leaveemployee_approve = LeaveReportEmployee.objects.filter(leave_status=1).count()
    leaveemployee_disapprove = LeaveReportEmployee.objects.filter(leave_status=2).count()

    context = {

        'blogs': blogs,
        'directors': directors,
        'categories': categories,
        'employee': employee,
        'leaveemployee': leaveemployee,
        'leaveemployee_approve': leaveemployee_approve,
        'leaveemployee_disapprove': leaveemployee_disapprove,

    }
    return context