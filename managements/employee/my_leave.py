from datetime import datetime
from http.client import HTTPResponse
from xml.dom import ValidationErr
from django.shortcuts import render, redirect
from accounts.models import User
from leave.models import LeaveReportEmployee

from managements.models import Employee
from django.core.paginator import Paginator
from django.contrib import messages
import pandas as pd
import numpy as np
from django.http import JsonResponse,HttpResponse

# using AJAX FORM SUBMISSION 
def leave_apply(request):
    if request.is_ajax():
        data ={}
        leave_reason = request.POST["leave_reason"]
        leave_start = request.POST["leave_start"]
        leave_end = request.POST["leave_end"]
        employee_obj = Employee.objects.get(user=request.user.id)
    return render(request, "managements/employee_template/employee_apply_leave.html")

""" 
EMPLOYEE APPLY FOR LEAVE
"""
def employee_apply_leave(request):
    employee_obj = Employee.objects.get(user=request.user.id)

    leave_data = (
        LeaveReportEmployee.objects.filter(employee=employee_obj).order_by("-updated_at").order_by("-created_at")
    )
    paginator = Paginator(leave_data, 5)
    page = request.GET.get("page")
    paged_leave_data = paginator.get_page(page)
    context = {
        "employee_obj": employee_obj,
        "leave_data": paged_leave_data,
        # "user":user
    }
    return render(request, "managements/employee_template/employee_apply_leave.html", context)


""" 
SAVE EMPLOYEE LEAVE TO DB   
"""

def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'



def employee_apply_leave_save(request):
    if  not request.user.user_type == 1:
        return HttpResponse('User type not found')
    else:
        if request.method == 'POST':
            leave_reason = request.POST["leave_reason"]
            leave_start = request.POST["leave_start"]
            leave_end = request.POST["leave_end"]

            employee_obj = Employee.objects.get(user=request.user.id)

            try:
                leave_report = LeaveReportEmployee(
                    employee=employee_obj,
                    leave_start=leave_start,
                    leave_end=leave_end,
                    leave_reason=leave_reason,
                    leave_status=0,
                )
                # now = datetime.today()
                # if leave_report.leave_start >= leave_report.leave_end:

                #     messages.error(request, "Leave Ending date must be greater than Leave Starting date")
                #     return redirect("leave")
                # leave_end = pd.to_datetime(leave_report.leave_end).date()
                # leave_start = pd.to_datetime(leave_report.leave_start).date()
                # leave_report.total_duration_days = np.busday_count(leave_start, leave_end, holidays=[leave_start, leave_end])

                leave_report.save()
                print('success')
                messages.success(request, "Successfully applied for leave")

                return redirect("employee_apply_leave")
                # return JsonResponse(leave_report)
            except:
                print("Error")
                messages.error(request, "Failed to apply for leave")
                return redirect("employee_apply_leave")
