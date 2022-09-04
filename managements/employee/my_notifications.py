from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render
from leave.models import NotificationEmployee
from managements.models import Employee


@csrf_exempt
def employee_fcmtoken_save(request):
    fcm_token = request.POST['fcm_token']

    try:
        employee = Employee.objects.get(user=request.user.id)
        employee.fcm_token = fcm_token
        employee.save()
        return HttpResponse('True')
    except:
        return HttpResponse('False')


def employee_all_notificaton(request):
    employee = Employee.objects.get(user = request.user.id)
    
    notifications = NotificationEmployee.objects.filter(employee_id=employee.id).order_by('-created_at')
    paginator               = Paginator(notifications,5)
    page                    = request.GET.get('page')
    paged_notifications         = paginator.get_page(page)
    context = {
        'notifications':paged_notifications,
        
    }
    return render (request,'managements/employee_template/employee_all_notificaton.html',context)

