from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import  messages
from directors.models import Director
from payroll.models import JobRole



def jobrole_page(request):
    if request.user.user_type != 5:
        return HttpResponse('You are not allowed to view this page')
    else:
       
        # get the hrm request 
        hrm = Director.objects.get(user=request.user.id)
        # filter the jobrole created by the hrm
        job_role = JobRole.objects.filter(director = hrm)

        # render the query set to the template
        context = {
            'director':hrm,
            'job_role':job_role
        }
    return render(request, 'payroll/hrm/jobrole.html',context)


def job_role_save(request):
    """
    ADDING JOB ROLE 
    """
    if request.user.user_type != 5:
        return HttpResponse('You are not allow to view this page')
    else:        
        if request.method !='POST':
            return HttpResponse('Method not allow')
        else:

            director = request.POST.get("director")       
            name = request.POST["name"]

            # saving to the job role model table
            job_role = JobRole.objects.create(name=name)

            # get the director user request     
            director = Director.objects.get(user=director)

            # then saving the director to the job_role
            job_role.director = director

            # then save the job role to the model table
            job_role.save()
            print('success')
            return redirect('jobrole_page')
        
