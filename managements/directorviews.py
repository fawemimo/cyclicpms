from django.shortcuts import render,redirect,reverse

# Create your views here.
from .forms import *
from django.contrib.auth import authenticate, login
from accounts.models import User, Profile
from .models import Employee, Admin, Company
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.http import HttpResponse,JsonResponse
import requests
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.views.decorators.csrf import csrf_exempt
from leave.models import *
from category.models import *

import json
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy
from category.forms import AddCategoryForEmployeeForm

# for selescting employees categories 

class AddCategoryForEmployeeListView(ListView):
    model               = AddCategoryForEmployee
    form_class          = AddCategoryForEmployeeForm
    context_object_name = 'addcategories'
    template_name       = 'category/add_category_for_employee.html'
    paginate_by         = 25
    
    
    
class AddCategoryForEmployeeCreateView(CreateView):
    model                   = AddCategoryForEmployee    
    form_class              = AddCategoryForEmployeeForm
    success_url             = reverse_lazy('add_category_list')
    template_name           = 'category/category_form.html'

def add_category_for_employee(request):
    employee_obj            = Employee.objects.all()
    level_id                = request.GET.get('level')    
    grades                  = Grade.objects.filter(level=level_id)
    levels                  = Level.objects.all()
    context = {
        'employee_obj':employee_obj,
        'levels':levels,
        'grades':grades,
    }    
    return render(request,'category/category_form.html',context ) 
    
def load_grades(request):
    
    if request.method != 'POST':
        return redirect ('add_category_for_employee')
    else:
        employee                      = request.POST['employee']
        employee_id                   = Employee.objects.get(id=employee)
        level                         = request.POST['level']
        level_id                      = Level.objects.get(id=level)
        grade                         = request.POST['grade']
        grade_id                      = Grade.objects.get(id=grade) 
        steps                       = request.POST['steps']
        step_id                           = Step.objects.get(id=steps) 
        annual_gross_pay               = request.POST['annual_gross_pay']
        annual_net_pay                 = request.POST['annual_net_pay']
        leave_allocation_days          = request.POST['leave_allocation_days']
        
        try:
            category = AddCategoryForEmployee(employee=employee_id,level=level_id,grade=grade_id,steps=step_id,annual_gross_pay=annual_gross_pay,annual_net_pay=annual_net_pay,leave_allocation_days=leave_allocation_days)
        
            category.save()
            messages.success(request,'Employee category added successfully')
            print('success')
            return redirect('add_category_list')
        except:
            print('failed')
            messages.error(request,'Failed to add employee category')
            return redirect('add_category_for_employee')
       
        
class AddCategoryForEmployeeUpdateView(UpdateView):
    model                   = AddCategoryForEmployee
    form_class              = AddCategoryForEmployeeForm
    success_url             = reverse_lazy('add_category_list')
    template_name           = 'category/category_form.html'
    
def load_grades(request):
    
    level_id                = request.GET.get('level')    
    grades                  = Grade.objects.filter(level_id=level_id)
    context = {
        'grades':grades,
    }
    return render(request,'category/category_form.html',context)

# for deleting employee category 

def employee_category_delete(request,employee_id):
    employee            = Employee.objects.get(id=employee_id)
    profile             = Profile.objects.get(user=request.user.id)
    if request.method == 'POST':
        employee.delete()
        messages.success(request,'User deleted successfully')
        return redirect('add_category_list')
    
    context = {
        'employee':employee_id,
        'profile':profile
    }
    return render(request,'category/add_category_for_employee.html',context)
    
# def add_category_employee(request):
#     levels          = Level.objects.all()
#     grades           = Grade.objects.all()
#     steps           =   Step.objects.all()
#     employee        = Employee.objects.all()
#     context = {
#         'levels':levels,
#         'grades':grades,
#         'steps':steps,
#         'employee':employee
        
#     }
#     return render (request,'category/add_category_for_employee.html',context)

# def get_json_level_data(request):
#     qs_val = list(Level.objects.values())
#     return JsonResponse({'data':qs_val})

# def get_json_model_data(request,*args, **kwargs):
#     selected_level = kwargs.get('grade')
#     obj_models = list(Grade.objects.filter(level__level= selected_level).values())
#     return JsonResponse({'data':obj_models})

# def save_add_category(request):
    
#     if request.is_ajax():
#         level                 = request.POST.get('level')
#         print(level)
#         grade                 = request.POST.get('grade')
#         print(grade)
#         steps                  = request.POST.get('steps')
#         annual_gross_pay      = request.POST.get('annual_gross_pay')
#         annual_net_pay        = request.POST.get('annual_net_pay')
#         leave_allocation_days = request.POST.get('leave_allocation_days')
#         category              = request.POST.get('category')
#         employee              = request.POST.get('employee')
#         employee_obj          = Employee.objects.get(user = employee)
#         level_obj             = Level.objects.get(level = level)
#         grade_obj                = Grade.objects.get(grade=grade, level__level=level_obj.level)
#         steps_obj             = Step.objects.get(step=steps)
        
#         AddCategoryForEmployee.objects.create(level=level_obj,grade=grade_obj,steps= steps_obj,employee=employee_obj,annual_gross_pay=annual_gross_pay,annual_net_pay=annual_net_pay,leave_allocation_days=leave_allocation_days,category=category)
        
#         return JsonResponse({'created':True})
    
#     else:
#         return JsonResponse({'created':False},save=False)
    

# Notification

def employee_send_notification(request):
    employees           = Employee.objects.all()
    profile             = Profile.objects.get(user=request.user.id)
    context = {
    'employees':employees,
    'profile':profile
    }
    return render(request,'managements/director_template/employee_notification.html',context)

@csrf_exempt
def send_employee_notification(request):

    id                  = request.POST.get("id")
    message             = request.POST.get("message")
    employee            = Employee.objects.get(user=id)
    token               = employee.fcm_token
    url                 = "https://fcm.googleapis.com/fcm/send"
    body                = {
                            "notification":{
                                "title":"Cylic Payroll Management System",
                                "body":message,
                                # "click_action": "https://studentmanagementsystem22.herokuapp.com/student_all_notification",
                                # "icon": "http://studentmanagementsystem22.herokuapp.com/static/dist/img/user2-160x160.jpg"
                            },
                            "to":token
                        }
    headers             = { 
                            "Content-Type":"application/json",
                            "Authorization":"key=AAAAhovrr00:APA91bF5Qy5AS5eDgrAv7-gEol8rjmcJx_kx021quajt9zNqfvfCH4puoOQyKeKbo9uSYuCx6gsawAoA81f1wvCMTA_kcR3b9c7K6rrWxhwrazA4geXTl5aMij3_rrs9E4LrIIrRYmLO "

    }
    data                =requests.post(url,data=json.dumps(body),headers=headers)
    notification        =NotificationEmployee(employee_id=employee,message=message)
    notification.save()
    # print(data.text)
    return HttpResponse("True")

# director editing profile

def director_profile(request):
    user                = User.objects.get(id=request.user.id)
    profile             = Profile.objects.get(user=request.user.id)
    
    
    context = {
    'user':user,
    'profile':profile

    }
    return render (request,'managements/director_template/director_profile.html',context)

def director_profile_save(request):
    if request.method != 'POST':

        return redirect('director_profile')


    else:

        first_name      = request.POST.get('first_name')
        last_name       = request.POST.get('last_name')
        other_name      = request.POST.get('other_name')
        password        = request.POST.get('password')


        try:
            user                = User.objects.get(id=request.user.id)
            user.first_name     = first_name
            user.last_name      = last_name
            user.other_name     = other_name
            if password != None and password != "":
                user.set_password(password)

            user.save()
            messages.success(request,'Profile change successfully')
            return redirect('accounts-logout')
        except:
            messages.error(request,'Failed to make changes')
            return redirect('director_profile')






# deleting employee

def delete_employee(request,employee_id):
    user        = User.objects.get(id=employee_id)
    profile     = Profile.objects.get(user=request.user.id)
    
    if request.method == 'POST':
        user.delete()
        messages.success(request,'User deleted successfully')
        return redirect('manage-employee')
    
    context = {
        'user':employee_id,
        'profile':profile,
    }
    return render (request,'managements/director_template/delete_user.html',context)
    

def addemployee(request):
    profile = Profile.objects.get(user=request.user.id)
    if request.method == 'POST':
        form                    = UserExtendedForm(request.POST)
        employee_form           = EmployeeForm(request.POST)
        
        if form.is_valid() and employee_form.is_valid():
            user = form.save()
            employee = employee_form.save(commit=False)
            employee.user = user
            
            employee.save()
            
            email = form.cleaned_data.get('email') 
            password = form.cleaned_data.get('password1')
            user = authenticate(username=email,password=password)
            print('its seem good')
            return redirect('directors')
        
    else:
        form                 = UserExtendedForm()
        employee_form        = EmployeeForm()
        
    context = {
        'form':form,
        'employee_form':employee_form
    }    
    return render (request,'managements/add_employee.html',context)

# views that render template for adding employees 

def add_employee(request):
    company = Company.objects.all()
    profile = Profile.objects.get(user=request.user.id)
    context = {
        'company':company,
        'profile':profile
    }
    return render(request,'managements/director_template/add_employee.html',context)


# views that save employees 

def add_employee_save(request):
    if request.method != 'POST':
        
        return HttpResponse('method not allowed')   
        
    else:
        first_name          = request.POST['first_name']
        last_name           = request.POST['last_name']
        other_name          = request.POST['other_name']
        username            = request.POST['username']
        email               = request.POST['email']
        password            = request.POST['password']
        phone_number        = request.POST['phone_number']
        phone_number_2      = request.POST['phone_number_2']
        contact_address     = request.POST['contact_address']
        company_name        = request.POST['company_name']
        department          = request.POST['department']
        dob                 = request.POST['dob']
        contact_address     = request.POST['contact_address']
        gender              = request.POST['gender']
        
        
        user = User.objects.create_user(username=username,first_name=first_name,last_name=last_name,other_name=other_name,email=email,password=password,phone_number=phone_number,user_type=1)
        
        user.save()
        # creating the models for employees 
        
        user.employee.phone_number_2    = phone_number_2
        user.employee.department        = department
        user.employee.dob               = dob
        user.employee.contact_address   = contact_address
        user.employee.gender            = gender
        user.employee.company_name      = company_name
        user.save()
       
        
        # creating the models for company 
        
        
        user.save()
        
        
        
        
        messages.success(request, first_name + last_name + ' added successfully')
        return redirect('manage-employee')
    
# for checking user email     

@csrf_exempt
def check_email_exist(request):
    email           = request.POST.get('email')
    user            = User.objects.filter(email=email).exists()
    if user:
        return HttpResponse(True)
    else:
        return HttpResponse(False)
    
@csrf_exempt
def check_username_exist(request):
    username        = request.POST.get('username')
    user            = User.objects.filter(username=username).exists()
    if user:
        return HttpResponse(True)
    else:
        return HttpResponse(False)
    
        
# manage employee 
def manage_employee(request):
    employees               = Employee.objects.order_by('-date_employed')
    profile                 = Profile.objects.get(user=request.user.id)
    queryset                = Employee.objects.all()
    querys                  = User.objects.all()
    form                    = EmployeeForm(request.POST)
    u_form                  = UserSearchForm(request.POST)
    paginator               = Paginator(employees,25)
    page                    = request.GET.get('page')
    paged_employees         = paginator.get_page(page)
    if request.method == 'POST':
        if form.is_valid():
            queryset   = Employee.objects.filter(department__icontains=form['department'].value(),
                                              employee_unique_id__icontains=form['employee_unique_id'].value())
            
    context = {
    'employees':paged_employees,
    'form':form,
    'profile':profile,
    'queryset':queryset,
    'u_form':u_form,
    'querys':querys
    
}
  
    return render(request,'managements/director_template/manage_employee.html',context)    

# editing employee 
def edit_employee(request,employee_id):
    employee            = Employee.objects.get(user_id=employee_id)
    profile             = Profile.objects.get(user=request.user.id)
    
    context = {
        'employee':employee,
        'id':employee_id,
        'profile':profile,
    }
    return render (request,'managements/director_template/edit_employee.html',context)

def edit_employee_save(request):
    if request.method != 'POST':
        messages.error(request,'method not allowed')
        return redirect('edit-employee')  
               
    else:
        employee_id         = request.POST['employee_id']     
        first_name          = request.POST['first_name']
        last_name           = request.POST['last_name']
        other_name          = request.POST['other_name']
        email               = request.POST['email']
        username            = request.POST['username']
        contact_address     = request.POST['contact_address']
        phone_number        = request.POST['phone_number']
        phone_number_2      = request.POST['phone_number_2']
        department          = request.POST['department']
        
        try:
            user                        = User.objects.get(id=employee_id)
            user.first_name             = first_name
            user.last_name              = last_name
            user.other_name             = other_name
            user.email                  = email
            user.username               = username
            user.phone_number           = phone_number
            user.save()
            # employee model to save 
            
            employee = Employee.objects.get(user=employee_id)
            employee.phone_number_2         = phone_number_2
            employee.contact_address        = contact_address
            employee.department             = department
            employee.save()
            messages.success(request,'Changes made successfully')
            return redirect('manage-employee')
                
        except:
            messages.error(request,'failed to edit')
            return redirect('edit-employee')
        
# employee feedback

def employee_feedback_message(request):
    feedbacks       = FeedBackEmployee.objects.all().order_by('-created_at')
    profile         = Profile.objects.get(user=request.user.id)
    
    paginator               = Paginator(feedbacks,25)
    page                    = request.GET.get('page')
    paged_feedbacks         = paginator.get_page(page)
    context = {
        'feedbacks':paged_feedbacks,
        'profile':profile
    }
    return render(request,'managements/director_template/employee_feedback.html',context)

@csrf_exempt
def employee_feedback_message_replied(request):

    feedback_id                  = request.POST.get('id')
    feedback_reply               = request.POST.get('message')
    
    try:
        feedbackemployee                    = FeedBackEmployee.objects.get(id=feedback_id)

        feedbackemployee.feedback_reply     = feedback_reply
        feedbackemployee.save()
        return HttpResponse('True')
    except:
        return HttpResponse('Fale')

            
def employee_leave_view(request):
    leaves              = LeaveReportEmployee.objects.order_by('-created_at')
    profile             = Profile.objects.get(user=request.user.id)
    
    paginator               = Paginator(leaves,25)
    page                    = request.GET.get('page')
    paged_leaves         = paginator.get_page(page)
    context = {
        'leaves':paged_leaves,
        'profile':profile

    }
    return render(request,'managements/director_template/employee_leave_view.html',context)
        
def employee_approve_leave(request,leave_id):
    leave                       = LeaveReportEmployee.objects.get(id=leave_id)
    leave.leave_status          = 1
    
    leave.save()
    
    return redirect('employee_leave_view')

def employee_disapprove_leave(request,leave_id):
    leave                   = LeaveReportEmployee.objects.get(id=leave_id)
    leave.leave_status      = 2
    leave.save()
    return redirect('employee_leave_view')



'''     
==================================================         
Admin control by directors 

views that render template for adding admin 
=====================================================

'''
def add_admin(request):
    profile = Profile.objects.get(user=request.user.id)
    context = {
        'profile':profile
    }
    return render(request,'managements/director_template/add_admin.html',context)


# views that save admin 

def add_admin_save(request):
    if request.method != 'POST':
        
        return HttpResponse('method not allowed')   
        
    else:
        first_name          = request.POST['first_name']
        last_name           = request.POST['last_name']
        other_name          = request.POST['other_name']
        username            = request.POST['username']
        email               = request.POST['email']
        password            = request.POST['password']
        phone_number        = request.POST['phone_number']
        phone_number_2      = request.POST['phone_number_2']
        contact_address     = request.POST['contact_address']
        company_name        = request.POST['company_name']
        department          = request.POST['department']
        dob                 = request.POST['dob']
        contact_address     = request.POST['contact_address']
        gender              = request.POST['gender']
        
        
        user = User.objects.create_user(username=username,first_name=first_name,last_name=last_name,other_name=other_name,email=email,password=password,phone_number=phone_number,user_type=2)
        
        user.save()
        
        # creating the models for employees 
        
        user.admin.phone_number_2    = phone_number_2
        user.admin.department        = department
        user.admin.dob               = dob
        user.admin.contact_address   = contact_address
        user.admin.gender            = gender
        user.admin.company_name      = company_name
        user.save()
       
        
        # creating the models for company 
        
        
        user.save()
        
        
        
        
        messages.success(request, first_name  +  last_name + ' added successfully')
        return redirect('manage_admin')
    
    
# manage admin

 
def manage_admin(request):
    admins                  = Admin.objects.order_by('-date_employed')
    profile                 = Profile.objects.get(user=request.user.id)
    
    form                    = AdminForm(request.POST or None)
    department              = request.POST.get('department')
    admin_unique_id         = request.POST.get('admin_unique_id')
    queryset = Admin.objects.all()
    # page paginator  
    
    paginator               = Paginator(admins,25)
    page                    = request.GET.get('page')
    paged_admins            = paginator.get_page(page)
    if request.method == 'POST':
        queryset   = Admin.objects.filter(department__icontains=form['department'].value(),
                                              admin_unique_id__icontains=form['admin_unique_id'].value())
   
    context = {
        'admins':paged_admins,
        'form':form,
        'profile':profile,
        'queryset':queryset
    }
    return render(request,'managements/director_template/manage_admin.html',context)    



# editing admin 
def edit_admin(request,admin_id):
    admin               = Admin.objects.get(user_id=admin_id)
    profile             = Profile.objects.get(user=request.user.id)
    
    context = {
        'admin':admin,
        'id':admin_id,
        'profile':profile
    }
    return render (request,'managements/director_template/edit_admin.html',context)



def edit_admin_save(request):
    if request.method != 'POST':
        messages.error(request,'method not allowed')
        return redirect('edit-admin')  
               
    else:
        admin_id            = request.POST['admin_id']     
        first_name          = request.POST['first_name']
        last_name           = request.POST['last_name']
        other_name          = request.POST['other_name']
        email               = request.POST['email']
        username            = request.POST['username']
        contact_address     = request.POST['contact_address']
        phone_number        = request.POST['phone_number']
        phone_number_2      = request.POST['phone_number_2']
        department          = request.POST['department']
        
        try:
            user                        = User.objects.get(id=admin_id)
            user.first_name             = first_name
            user.last_name              = last_name
            user.other_name             = other_name
            user.email                  = email
            user.username               = username
            user.phone_number           = phone_number
            user.save()
            
            
            # admin model to save 
            
            admin                        = Admin.objects.get(user=admin_id)
            admin.phone_number_2         = phone_number_2
            admin.contact_address        = contact_address
            admin.department             = department
            admin.save()
            messages.success(request,'Changes made successfully')
            return redirect('manage_admin')
                
        except:
            messages.error(request,'failed to edit')
            return redirect('edit_admin')
        
def delete_admin(request,admin_id):
    user            = User.objects.get(id=admin_id)
    profile         = Profile.objects.get(user=request.user.id)
    if request.method == 'POST':
        user.delete()
        messages.success(request,'User deleted successfully')
        return redirect('manage_admin')
    
    context = {
        'user':admin_id,
        'profile':profile
    }
    return render (request,'managements/director_template/delete_admin.html',context)
