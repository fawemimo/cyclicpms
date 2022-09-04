import imp
import json
from operator import ipow
from django.http import HttpResponse
from django.shortcuts import render,redirect
from directors.models import Director

from leave.models import NotificationEmployee
from managements.models import Employee
from django.core.paginator import Paginator
from django.views.decorators.csrf import csrf_exempt
import requests
from django.db.models import Q


'''
EMPLOYEE NOTIFICATIONS FUNCTIONALITY
'''
def director_send_notification_employee(request):
    if not request.user.user_type == 5:
        return HttpResponse('You are not allow to view this page')
    else:

        directors = Director.objects.get(user=request.user.id)
        employees = Employee.objects.filter(
            director=directors).order_by('-date_employed')

        paginator = Paginator(employees, 25)
        page = request.GET.get('page')
        paged_employees = paginator.get_page(page)
        context = {
            'employees': paged_employees,

            # 'directors':directors
        }
        return render(request, 'managements/director_template/employee_notification.html', context)



""" 
SEND NOTIFICATION
"""
@csrf_exempt
def send_employee_notification(request):
    if not request.user.user_type == 5:
        return HttpResponse('You are not allow to view this page')
    else:

        id = request.POST.get("id")
        message = request.POST.get("message")
        employee = Employee.objects.get(user=id)
        token = employee.fcm_token
        url = "https://fcm.googleapis.com/fcm/send"
        body = {
            "notification": {
                "title": "Cylic Payroll Management System",
                "body": message,
                "click_action": "https://cyclicpms.herokuapp.com/managements/employee_all_notificaton",
                "icon": "https://payrollmgt-bucket.s3.amazonaws.com/static/media/20200804_150827.jpg"
            },
            "to": token
        }
        headers = {
            "Content-Type": "application/json",
            "Authorization": "key=AAAAhovrr00:APA91bF5Qy5AS5eDgrAv7-gEol8rjmcJx_kx021quajt9zNqfvfCH4puoOQyKeKbo9uSYuCx6gsawAoA81f1wvCMTA_kcR3b9c7K6rrWxhwrazA4geXTl5aMij3_rrs9E4LrIIrRYmLO "

        }
        data = requests.post(url, data=json.dumps(body), headers=headers)
        notification = NotificationEmployee(
            employee_id=employee, message=message)
        notification.save()
        # print(data.text)
        return HttpResponse("True")


'''
EMPLOYEE NOTIFICATIONS SEARCH

'''

def search_notify(request):
    if not request.user.user_type == 5:
        return HttpResponse('You are not allow to view this page')
    else:
        if 'keywords' in request.GET:
            keywords = request.GET['keywords']
            if keywords:
                director = Director.objects.get(user=request.user.id)
                employees = Employee.objects.filter(director=director).filter(Q(user__first_name__icontains=keywords) | Q(
                    user__last_name__icontains=keywords) | Q(user__last_name__icontains=keywords)).order_by('-date_employed')

                paginator = Paginator(employees, 25)
                page = request.GET.get('page')
                paged_employees = paginator.get_page(page)
                total = employees.count()

            context = {
                'employees': paged_employees,
                'total': total,

                # 'directors':directors
            }

        return render(request, 'managements/director_template/employee_notification.html', context)
