from django.shortcuts import render,redirect
from leave.models import LeaveReportEmployee

from managements.models import Employee
from django.core.paginator import Paginator
from django.contrib import messages


""" 
EMPLOYEE APPLY FOR LEAVE
"""
def employee_apply_leave(request):    
    employee_obj = Employee.objects.get(user=request.user.id)
    leave_data = LeaveReportEmployee.objects.filter(employee=employee_obj).order_by('-updated_at').order_by('-created_at')
    paginator               = Paginator(leave_data,5)
    page                    = request.GET.get('page')
    paged_leave_data         = paginator.get_page(page)
    context = {
        'employee_obj':employee_obj,
        'leave_data':paged_leave_data,
        
    }
    return render(request,'managements/employee_template/employee_apply_leave.html',context)


""" 
SAVE EMPLOYEE LEAVE TO DB   
"""
def employee_apply_leave_save(request):
    if request.method != 'POST':
        return redirect('employee_apply_leave')
    else:
        
        leave_reason = request.POST['leave_reason']
        leave_start = request.POST['leave_start']
        leave_end = request.POST['leave_end']
        
        
        employee_obj = Employee.objects.get(user=request.user.id)
        
        try:
            leave_report = LeaveReportEmployee(employee = employee_obj,leave_start=leave_start,leave_end=leave_end,leave_reason=leave_reason,leave_status=0)
            leave_report.save()
            messages.success(request,'Successfully applied for leave ' )
            
            return redirect('employee_apply_leave')
        except:
            messages.error(request,'Failed to apply for leave')
            return redirect('employee_apply_leave')