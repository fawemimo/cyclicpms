from django.shortcuts import render, reverse, redirect
from leave.models import LeaveReportEmployee, FeedBackEmployee, NotificationEmployee
from managements.models import *
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt



def employee_apply_leave(request):
    employee_obj = Employee.objects.get(user=request.user.id)
    leave_data = LeaveReportEmployee.objects.filter(employee=employee_obj).order_by('-created_at')
    
    context = {
        'employee_obj':employee_obj,
        'leave_data':leave_data
    }
    return render(request,'managements/employee_template/employee_apply_leave.html',context)

def employee_apply_leave_save(request):
    if request.method != 'POST':
        return redirect('employee_apply_leave')
    else:
        leave_date = request.POST['leave_date']
        leave_reason = request.POST['leave_reason']
        
        
        employee_obj = Employee.objects.get(user=request.user.id)
        
        try:
            leave_report = LeaveReportEmployee(employee = employee_obj,leave_date=leave_date,leave_reason=leave_reason,leave_status=0)
            leave_report.save()
            messages.success(request,'Successfully applied for leave ' )
            
            return redirect('employee_apply_leave')
        except:
            messages.error(request,'Failed to apply for leave')
            return redirect('employee_apply_leave')
        
        
def employee_feedback(request):
    employee_obj = Employee.objects.get(user=request.user.id)
    feedback_data = FeedBackEmployee.objects.filter(employee=employee_obj).order_by('-created_at')
    context = {
        'employee_obj':employee_obj,
        'feedback_data':feedback_data
    }
    return render(request,'managements/employee_template/employee_feedback.html',context)

def employee_feedback_save(request):
    if request.method != 'POST':
        return redirect('employee_feedback')
    else:
        feedback = request.POST['feedback']
        
        
        
        employee_obj = Employee.objects.get(user=request.user.id)
        
        try:
            feedback_report = FeedBackEmployee(employee = employee_obj,feedback=feedback,feedback_reply="")
            feedback_report.save()
            messages.success(request,'Successfully sent Feed Back ')
            
            return redirect('employee_feedback')
        except:
            messages.error(request,'Failed to send Feed Back')
            return redirect('employee_feedback')


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
    notifications = NotificationEmployee.objects.filter(employee_id=employee.id)
    context = {
        'notifications':notifications
    }
    return render (request,'managements/employee_template/employee_all_notificaton.html',context)

