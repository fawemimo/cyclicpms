import requests
from django.http import JsonResponse
from django.shortcuts import render

from managements.models import *

# from .models import Model
from .models import *


def main_view(request):
    qs = Car.objects.all()
    context = {
        'qs':qs
    }
    return render(request, 'category/main.html', context)

def main_view2(request):
    director         = Director.objects.get(user=request.user.id)
    qs               = Department.objects.filter(director=director)
    qs2              = Level.objects.filter(director=director)
    qs3              = Grade.objects.filter(director=director)
    qs4              = Step.objects.filter(director=director)
    qs5              = Leave.objects.filter(director=director)
    context = {
        'qs':qs,
        'qs2':qs2,
        'qs3':qs3,
        'qs4':qs4,
        'qs5':qs5
    }
    return render(request, 'category/main.html', context)



def get_json_car_data(request):
    qs_val = list(Car.objects.values())
    
    return JsonResponse({'data':qs_val})

def get_json_car_data2(request):
    director         = Director.objects.get(user=request.user.id)
    qs_val2          = list(Department.objects.filter(director=director).values())
    position         = list(Position.objects.filter(director=director).values())
    level            = list(Level.objects.filter(director=director).values())
    grade            = list(Grade.objects.filter(director=director).values())
    step             = list(Step.objects.filter(director=director).values())
    leave            = list(Leave.objects.filter(director=director).values())
    context = {
        'qs_val2':qs_val2,
        'position':position,
        'level':level,
        'grade':grade,
        'step':step,
        'leave':leave
    }
    return JsonResponse(context)

def get_json_model_data(request, *args, **kwargs):
    selected_car = kwargs.get('car')
    obj_models = list(Model.objects.filter(car__name=selected_car).values())
    return JsonResponse({'data':obj_models})


def get_json_position_data(request, *args, **kwargs):
    selected_department = kwargs.get('department')
    selected_position = kwargs.get('position')
    selected_grade = kwargs.get('grade')
    selected_step = kwargs.get('step')
    selected_leave = kwargs.get('leave')
    selected_level = kwargs.get('level')
    # obj_department = list(Department.objects.filter)
    obj_leave = list(Leave.objects.filter(step__name=selected_leave).values())
    obj_step = list(Step.objects.filter(grade__name=selected_step).values())
    obj_grade = list(Grade.objects.filter(level__name=selected_grade).values())
    obj_position = list(Position.objects.filter(department__name=selected_department).values())
    obj_level = list(Level.objects.filter(position__name=selected_position).values())
    
    context = {
        'position':obj_position,
        'level':obj_level,
        'grade':obj_grade,
        'step':obj_step,
        'leave':obj_leave        
    }
    return JsonResponse(context)

# for position 

def get_json_level_data(request,*args, **kwargs):
    selected_position = kwargs.get('position')
    obj_level = list(Level.objects.filter(position__name=selected_position).values())
    context = {
        'level':obj_level
    }
    return JsonResponse(context)

# for level 

# for grades  /

def get_json_grade_data(request,*args, **kwargs):
    selected_grade = kwargs.get('grade')
    obj_grade = list(Grade.objects.filter(level__name=selected_grade).values())
    context = {
        'grade':obj_grade
    }
    return JsonResponse(context)

# for steps /
def get_json_step_data(request,*args, **kwargs):
    selected_step = kwargs.get('step')
    obj_step = list(Step.objects.filter(grade__name=selected_step).values())
    context = {
        'step':obj_step
    }
    return JsonResponse(context)

# for leave days 

def get_json_leave_data(request,*args, **kwargs):
    selected_leave = kwargs.get('leave')
    obj_leave = list(Leave.objects.filter(step__name=selected_leave).values())
    context = {
        'leave':obj_leave
    }
    return JsonResponse(context)
    
def add_category(request):
    if request.is_ajax():
        director            = request.POST.get('director')
        dir_obj             = Director.objects.get(user=director)
        department          = request.POST.get('department')
        department_obj      = Department.objects.get(name=department)
        position            = request.POST.get('position')
        position_obj           = Position.objects.get(name=position)
        level               = request.POST.get('level')
        level_obj           = Level.objects.get(name=level)
        grade               = request.POST.get('grade')
        grade_obj           = Grade.objects.get(name=grade)
        step                = request.POST.get('step')
        step_obj            = Step.objects.get(name=step)
        leave               = request.POST.get('days')
        leave_obj              = Leave.objects.get(days=leave)
        
        AddCategory.objects.create(director=dir_obj,department=department_obj,position=position_obj,level=level_obj,grade=grade_obj,step=step_obj,leave=leave_obj)
        return JsonResponse({'created':True})
    return JsonResponse({'created':True}, safe=False)
        
def create_order(request):
    if request.is_ajax():
        car = request.POST.get('car')
        car_obj = Car.objects.get(name=car)
        model = request.POST.get('model')
        model_obj = Model.objects.get(name=model, car__name=car_obj.name)
        Order.objects.create(car=car_obj, model=model_obj)
        return JsonResponse({'created': True})
    return JsonResponse({'created': False})

def create_order2(request):
    if request.is_ajax():
        car = request.POST.get('car')
        car_obj = Department.objects.get(name=car)
        model = request.POST.get('model')
        model_obj = Position.objects.get(name=model, car__name=car_obj.name)
        AddCategory.objects.create(car=car_obj, model=model_obj)
        return JsonResponse({'created': True})
    return JsonResponse({'created': False})

# def main_view(request):
#     qs = Car.objects.all()
#     qs2 = Level.objects.all()
#     context = {
#         'qs':qs,
#         'qs2':qs2
#     }
#     return render(request, 'category/main.html', context)

# def traditional_view(request):
#     qs1 = Car.objects.all()
#     qs2 = Model.objects.all()
#     return render(request, 'orders/t.html', {'qs1':qs1, 'qs2':qs2})

# def get_json_car_data(request):
#     qs_val = list(Car.objects.values())
#     qs_val2 = list(Level.objects.values())
#     context = {
#         'qs_val':qs_val,
#         'qs_val2':qs_val2
#     }
#     return JsonResponse({'data':qs_val})

# def get_json_model_data(request, *args, **kwargs):
#     selected_car = kwargs.get('car')
#     obj_models = list(Model.objects.filter(car__name=selected_car).values())
#     obj_models2 = list(Grade.objects.filter(level__name=selected_car).values())
#     return JsonResponse({'data':obj_models})

# def create_order(request):
#     if request.is_ajax():
#         car = request.POST.get('car')
#         car_obj = Car.objects.get(name=car)
#         model = request.POST.get('model')
#         model_obj = Model.objects.get(name=model, car__name=car_obj.name)
#         Order.objects.create(car=car_obj, model=model_obj)
#         return JsonResponse({'created': True})
#     return JsonResponse({'created': False})






