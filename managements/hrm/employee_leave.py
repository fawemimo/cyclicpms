from django.http import HttpResponse
from django.shortcuts import redirect,render

from directors.models import Director
from leave.models import LeaveReportEmployee
from django.core.paginator import Paginator
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt


""" 
EMPLOYEE LEAVE LIST
"""
def employee_leave_view(request):
    if not request.user.user_type == 5:
        return HttpResponse('You are not allow to view this page')
    else:

        leaves = LeaveReportEmployee.objects.order_by('-created_at')

        paginator = Paginator(leaves, 25)
        page = request.GET.get('page')
        paged_leaves = paginator.get_page(page)
        context = {
            'leaves': paged_leaves,
        }
        return render(request, 'managements/director_template/employee_leave_view.html', context)

""" 
APPROVE LEAVE
"""
def employee_approve_leave(request, leave_id):
    if not request.user.user_type == 5:
        return HttpResponse('You are not allow to view this page')
    else:
        leave = LeaveReportEmployee.objects.get(id=leave_id)
        leave.leave_status = 1

        leave.save()

        return redirect('employee_leave_view')

""" 
DISAPPROVE LEAVE 
"""


def employee_disapprove_leave(request, leave_id):
    if not request.user.user_type == 5:
        return HttpResponse('You are not allow to view this page')
    else:
        leave = LeaveReportEmployee.objects.get(id=leave_id)
        leave.leave_status = 2
        leave.save()
        return redirect('employee_leave_view')


""" 
SEARCH LEAVE
"""      

def search_leave(request):
    if not request.user.user_type == 5:
        return HttpResponse('You are not allow to view this page')
    else:
        if 'keyword' in request.GET:
            keyword = request.GET['keyword']
            if keyword:
                director = Director.objects.get(user=request.user.id)
                leaves = LeaveReportEmployee.objects.filter(employee__director=director).filter(Q(employee__user__first_name__icontains=keyword) | Q(
                    leave_reason__icontains=keyword) | Q(employee__user__last_name__icontains=keyword)).order_by('-created_at')
                paginator = Paginator(leaves, 25)
                page = request.GET.get('page')
                paged_leaves = paginator.get_page(page)
                total = leaves.count()

            context = {
                'leaves': paged_leaves,
                'total': total,

                # 'directors':directors
            }
        return render(request, 'managements/director_template/employee_leave_view.html', context)