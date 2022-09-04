from directors.models import Director
from managements.models import Employee


def hrm_context(request):
    director = Director.objects.all()
    employee = Employee.objects.all().filter(director=director)
    print(employee)
    # return render(request,'dashboards/director_template/director.html')