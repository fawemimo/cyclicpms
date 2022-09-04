from django.contrib import messages
from django.shortcuts import redirect, render
from leave.models import FeedBackEmployee

from managements.models import Employee


def employee_feedback(request):
    
    employee_obj = Employee.objects.get(user=request.user.id)
    feedback_data = FeedBackEmployee.objects.filter(employee=employee_obj).order_by('-created_at')
    context = {
        'employee_obj':employee_obj,
        'feedback_data':feedback_data,
        
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