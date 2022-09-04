from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.db.models import Q
'''

search query for any keyword for employee
'''

from directors.models import Director
from managements.models import Employee


def search_query(request):
    if not request.user.user_type == 5:
        return HttpResponse('You are not allow to view this page')
    else:

        # keywords
        if 'keyword' in request.GET:
            keyword = request.GET['keyword']
            if keyword:
                director = Director.objects.get(user=request.user.id)
                employees = Employee.objects.filter(director=director).filter(Q(user__first_name__icontains=keyword) | Q(
                    user__last_name__icontains=keyword) | Q(employee_unique_id__iexact=keyword))
                paginator = Paginator(employees, 5)
                page = request.GET.get('page')
                paged_employees = paginator.get_page(page)
                total = employees.count()

            context = {
                'employees': paged_employees,
                'total': total,

                # 'directors':directors
            }
        return render(request, 'managements/director_template/manage_employee.html', context)
