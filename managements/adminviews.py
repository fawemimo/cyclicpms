# from accounts.models import Profile
from django.contrib import messages
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http import HttpResponse
from django.shortcuts import redirect, render, reverse
from django.views.decorators.csrf import csrf_exempt

from leave.models import FeedBackAdmin, LeaveReportAdmin, NotificationAdmin
from managements.models import *


def admin_apply_leave(request):
    
    admin_obj               = Admin.objects.get(user=request.user.id)
    leave_data              = LeaveReportAdmin.objects.filter(admin=admin_obj).order_by('-created_at')
    paginator               = Paginator(leave_data,5)
    page                    = request.GET.get('page')
    paged_leave_data        = paginator.get_page(page)
    context = {
        'admin_obj':admin_obj,
        'leave_data':paged_leave_data,
        
    }
    return render(request,'managements/admin_template/admin_apply_leave.html',context)

def admin_apply_leave_save(request):
    if request.method != 'POST':
        return redirect('admin_apply_leave')
    else:
        leave_date          = request.POST['leave_date']
        leave_reason        = request.POST['leave_reason']
        leave_start         = request.POST['leave_start']
        leave_end           = request.POST['leave_end']
        
        admin_obj           = Admin.objects.get(user=request.user.id)
        
        try:
            leave_report    = LeaveReportAdmin(admin = admin_obj,leave_date=leave_date,leave_reason=leave_reason,leave_status=0,leave_start=leave_start,leave_end=leave_end)
            
            leave_report.save()
            messages.success(request,'Successfully applied for leave, we will get back to you as soon as possible' )
            
            return redirect('admin_apply_leave')
        except:
            messages.error(request,'Failed to apply for leave')
            return redirect('admin_apply_leave')
        
        
def admin_feedback(request):
    admin_obj               = Admin.objects.get(user=request.user.id)
    
    feedback_data           = FeedBackAdmin.objects.filter(admin=admin_obj).order_by('-created_at')
    context = {
        'admin_obj':admin_obj,
        'feedback_data':feedback_data,
        
    }
    return render(request,'managements/admin_template/admin_feedback.html',context)

def admin_feedback_save(request):
    if request.method != 'POST':
        return redirect('admin_feedback')
    else:
        feedback            = request.POST['feedback']
        
        admin_obj           = Admin.objects.get(user=request.user.id)
        
        try:
            feedback_report = FeedBackAdmin(admin = admin_obj,feedback=feedback,feedback_reply="")
            feedback_report.save()
            messages.success(request,'Successfully sent Feed Back ')
            
            return redirect('admin_feedback')
        except:
            messages.error(request,'Failed to send Feed Back')
            return redirect('admin_feedback')


@csrf_exempt
def admin_fcmtoken_save(request):
    fcm_token = request.POST['fcm_token']

    try:
        admin = Admin.objects.get(user=request.user.id)
        admin.fcm_token = fcm_token
        admin.save()
        return HttpResponse('True')
    except:
        return HttpResponse('False')


def admin_all_notificaton(request):
    admin = Admin.objects.get(user = request.user.id)
    
    notifications                   = NotificationAdmin.objects.filter(admin_id=admin.id).order_by('-created_at')
    paginator                       = Paginator(notifications,25)
    page                            = request.GET.get('page')
    paged_notifications             = paginator.get_page(page)
    context = {
        'notifications':paged_notifications,
        
    }
    return render (request,'managements/admin_template/admin_all_notificaton.html',context)

