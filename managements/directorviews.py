import csv
import json

import requests
# import xlsxwriter
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Q
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render, reverse
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import CreateView, ListView, UpdateView, View

from accounts.models import User
from category.forms import AddCategoryForEmployeeForm
from category.models import *
from dashboards.directorviews import director
from directors.models import *
from leave.models import *
from payroll.forms import PayrollManagerForm, PayrollManagerUploadForm
from payroll.models import PayrollManagerUpload

# Create your views here.
from .forms import *
from .models import *

'''
SETTING UP DASHBOARD TO ADD DEPARTMENT, POSITION,LEVEL,GRADE,STEP AND LEAVE
'''
""" # Director home page /
def director_homepage(request):
    director         = Director.objects.get(user=request.user.id)
    employee         = Employee.objects.all().filter(director=director).count()
    # admin            = Admin.objects.filter(director=director).count()
    # leaveadmin       = LeaveReportAdmin.objects.get(leave_status=0).count()
    leaveemployee    = LeaveReportEmployee.objects.filter(leave_status=0).count()
    
    context = {
        'director': director,
        'employee': employee,
        # 'leaveadmin':leaveadmin,
        'leaveemployee':leaveemployee
    }
    
    return render(request, 'dashboards/director_template/director.html',context) """

# adding leave


def leave(request):
    if not request.user.user_type == 5:
        return HttpResponse('You are not allow to view this page')
    else:
        director = Director.objects.get(user=request.user.id)
        leaves = Leave.objects.filter(
            director=director).order_by('-date_created')
        steps = Step.objects.filter(
            director=director).order_by('-date_created')

        context = {
            'leaves': leaves,
            'steps': steps
        }
    return render(request, 'category/leave.html', context)

# creating leave days for sub-steps


def create_leave(request):
    if not request.user.user_type == 5:
        return HttpResponse('You are not allow to view this page')
    else:
        if request.method != 'POST':
            print('failed')
        else:
            director = request.POST.get('director')
            days = request.POST['days']
            step = request.POST.get('step')

            # try:
            # saving the step into the table
            step_obj = Step.objects.get(id=step)
            # saving the director into the table
            dir_obj = Director.objects.get(user=director)
            # creating the level into the table
            leave = Leave.objects.create(
                days=days, step=step_obj, director=dir_obj)

            leave.save()
            print('success')
            messages.success(request, 'Leave successfully added')
            return redirect('leavess')
            # except:
            #     print('failed')
    return render(request, 'category/leave.html')


# adding steps
def step(request):
    if not request.user.user_type == 5:
        return HttpResponse('You are not allow to view this page')
    else:
        director = Director.objects.get(user=request.user.id)
        steps = Step.objects.filter(
            director=director).order_by('-date_created')
        grades = Grade.objects.filter(
            director=director).order_by('-date_created')

        context = {
            'steps': steps,
            'grades': grades
        }
    return render(request, 'category/step.html', context)

# creating steps for sub-grades


def create_step(request):
    if not request.user.user_type == 5:
        return HttpResponse('You are not allow to view this page')
    else:
        if request.method != 'POST':
            print('failed')
        else:
            director = request.POST.get('director')
            name = request.POST['name']
            grade = request.POST['grade']

            # try:
            # saving the grade into the table
            grade_obj = Grade.objects.get(id=grade)
            # saving the director into the table
            dir_obj = Director.objects.get(user=director)
            # creating the level into the table
            step = Step.objects.create(
                name=name, grade=grade_obj, director=dir_obj)

            step.save()

            messages.success(request, 'Level successfully added')
            return redirect('step')
    return render(request, 'category/step.html')

# adding grade


def grade(request):
    if not request.user.user_type == 5:
        return HttpResponse('You are not allow to view this page')
    else:
        director = Director.objects.get(user=request.user.id)
        grades = Grade.objects.filter(
            director=director).order_by('-date_created')
        levels = Level.objects.filter(
            director=director).order_by('-date_created')

        context = {
            'grades': grades,
            'levels': levels
        }

    return render(request, 'category/grade.html', context)

# creting grades for each sub-level


def create_grade(request):
    if not request.user.user_type == 5:
        return HttpResponse('You are not allow to view this page')
    else:
        if request.method != 'POST':
            print('failed')
        else:
            director = request.POST.get('director')
            name = request.POST['name']
            level = request.POST['level']

            # try:
            # saving the level into the table
            level_obj = Level.objects.get(id=level)
            # saving the director into the table
            dir_obj = Director.objects.get(user=director)
            # creating the level into the table
            grade = Grade.objects.create(
                name=name, level=level_obj, director=dir_obj)

            grade.save()

            messages.success(request, 'Level successfully added')
            return redirect('grade')
            # except:
            #     print('Failed')
    return render(request, 'category/grade.html')
# add level


def level(request):
    # // check the user_type here first.

    if not request.user.user_type == 5:
        return HttpResponse('You are not allow to view this page')
    else:

        director = Director.objects.get(user=request.user.id)
        levels = Level.objects.filter(
            director=director).order_by('-date_created')
        positions = Position.objects.filter(
            director=director).order_by('-date_created')

        context = {
            'levels': levels,
            'positions': positions,
            'director': director
        }
    return render(request, 'category/level.html', context)

# creating level /


def create_level(request):
    if not request.user.user_type == 5:
        return HttpResponse('You are not allow to view this page')
    else:
        if request.method != 'POST':
            print('failed')
        else:
            director = request.POST.get('director')
            name = request.POST.get('name')
            position = request.POST.get('position')

            # try:
            # saving the position into the table
            pos_obj = Position.objects.get(id=position)
            # saving the director into the table
            dir_obj = Director.objects.get(user=director)
            # creating the level into the table
            level = Level.objects.create(
                name=name, position=pos_obj, director=dir_obj)

            level.save()
            messages.success(request, 'Level successfully added')
            return redirect('level')
    return render(request, 'category/level.html')


# aading position /
def position(request):
    if request.user.user_type == 5:

        director = Director.objects.get(user=request.user.id)
        positions = Position.objects.filter(
            director=director).order_by('-date_created')
        departments = Department.objects.filter(
            director=director).order_by('-date_created')
        context = {
            'positions': positions,
            'departments': departments,
            'director': director
        }
        return render(request, 'category/position.html', context)
    else:
        return HttpResponse('You are not allow to view this page')


# creating position

def create_position(request):
    if request.method == 'POST':
        director = request.POST.get('director')
        name = request.POST['name']
        department = request.POST['department']
        dep_obj = Department.objects.get(name=department)
        director_obj = Director.objects.get(user=director)
        position = Position.objects.create(
            name=name, department=dep_obj, director=director_obj)

        position.save()
        messages.success(request, 'Position added successfully')

        return redirect('position')
    else:

        messages.error(request, 'Position failed to add')
    return render(request, 'category/position.html')

# editing or updating position


def edit_position(request, position_id):
    if not request.user.user_type == 5:
        return HttpResponse('You are not allow to view this page')
    else:
        positions = Position.objects.get(department=position_id)
        departments = Department.objects.get(id=position_id)
        context = {
            'positions': positions,
            'id': position_id,
            'departments': departments
        }

    return render(request, 'category/position.html', context)


def edit_position_save(request, position_id):
    if not request.user.user_type == 5:
        return HttpResponse('Page not found!')
    else:
        if request.method != 'POST':
            messages.error(request, 'method not allowed')
            print('error')

        else:

            name = request.POST.get('name')
            department = request.POST.get('department')

            try:
                # saving the department into department table
                department = Department.objects.get(id=position_id)
                department.department = department
                department.save()

                # saving the name to position table

                position = Position.objects.get(department=position_id)
                position.name = name
                position.save()

                print('success')
            except:
                print('failed')


# adding department
def department(request):
    if not request.user.user_type == 5:
        return HttpResponse('You are not allow to view this page')
    else:
        director = Director.objects.get(user=request.user.id)
        departments = Department.objects.filter(
            director=director).order_by('-date_created')

        context = {
            'departments': departments,
            'director': director,

        }

    return render(request, 'category/department.html', context)

# creating department


def create_department(request):
    if not request.user.user_type == 5:
        return HttpResponse('You are not allow to view this page')
    else:

        directors = Director.objects.get(user=request.user.id)

        context = {


            'directors': directors
        }
        return render(request, 'category/department.html', context)


def create_department_save(request):
    if not request.user.user_type == 5:
        return HttpResponse('Page not found!')
    else:
        if request.method != 'POST':
            return HttpResponse('Method not allowed')
        else:
            director = request.POST.get('director')
            name = request.POST.get('name')

            department = Department.objects.create(
                name=name,
            )
            director_obj = Director.objects.get(user=director)
            department.director = director_obj
            department.save()

            # print('success')
            messages.success(request, 'Department added successfully')
            return redirect('department')

# updating department


def update_department(request, department_id):
    if not request.user.user_type == 5:
        return HttpResponse('Page not found')
    else:

        directors = Director.objects.get(user=request.user.id)
        department = Department.objects.get(id=department_id)
        context = {


            'directors': directors,
            'department': department
        }

    return render(request, 'category/department.html', context)


def update_department_save(request):
    if not request.user.user_type == 5:
        return HttpResponse('Page not found!')
    else:
        if request.method != 'POST':
            return HttpResponse('method not allow')
        else:
            department_id = request.POST['department_id']
            director = request.POST.get('director')
            name = request.POST.get('name')

            # try:
            dep_obj = Department.objects.get(id=department_id)

            dep_obj.name = name
            dep_obj.director = director
            dep_obj.save()
            print('success')
            return redirect('department')
            # except:
            #     print('Failed')


class UpdateDepartment(View):
    def get(self, request):
        id = request.GET.get('id', None)
        name = request.GET.get('name', None)

        obj = Department.objects.get(id=id)
        obj.name = name

        obj.save()

        department = {'id': obj.id, 'name': obj.name}

        data = {
            'department': department
        }
        return JsonResponse(data)

# deleting department


class DeleteDepartment(View):
    def get(self, request):
        id = request.GET.get('id', None)
        Department.objects.get(id=id).delete()
        data = {
            'deleted': True
        }
        return JsonResponse(data)


'''
END SETTING UP DASHBOARD TO ADD DEPARTMENT, POSITION,LEVEL,GRADE,STEP AND LEAVE
'''




'''
checking for emails and username for both employees and admins
'''



'''
ADDING EMPLOYEE CATEGORIES
'''

# for selescting employees categories


def add_category_view(request):
    if not request.user.user_type == 5:
        return HttpResponse('You are not allow to view this page')
    else:
        director = Director.objects.get(user=request.user.id)
        category = AddCategory.objects.filter(director=director)
        employee = Employee.objects.filter(director=director)

        context = {
            'category': category,
            'employee': employee,

        }
    return render(request, 'category/add_category_for_employee.html', context)

# for category updates/edit  /


def update_category(request, category_id):
    if not request.user.user_type == 5:
        return HttpResponse('You are not allow to view this page')
    else:
        # employee            = Employee.objects.get(user=category_id)

        category = AddCategory.objects.get(employee=category_id)

        context = {
            'category': category,

        }
        return render(request, 'category/update_category.html', context)


'''
END ADDING EMPLOYEE CATEGORIES
'''


'''
EMPLOYEE PROFILE TEMPLATE
'''


def all_staff_profile(request):
    # check if it is the director login request
    if not request.user.user_type == 5:
        return HttpResponse('You are not allow to view this page')
    else:
        directors = Director.objects.get(user=request.user.id)
        employees = Employee.objects.filter(
            director=directors).order_by('-date_employed')
        paginator = Paginator(employees, 25)
        page = request.GET.get('page')
        paged_employees = paginator.get_page(page)

        context = {
            'employees': paged_employees
        }

    return render(request, 'managements/director_template/all_staff_profile.html', context)


def all_staff_profile_template(request, employee_id):
    # check if it is director
    if not request.user.user_type == 5:
        return HttpResponse('You are not allow to view this page')
    else:
        directors = Director.objects.get(user=request.user.id)
        user = User.objects.filter(id=employee_id)
        # profile                 = Profile.objects.get(user=employee_id)

        context = {
            'user': user,
            #
        }
        return render(request, 'managements/director_template/all_staff_profile_template.html', context)


'''
EMPLOYEE PROFILE TEMPLATE
'''








# views for payroll manager  /
def payroll_manager(request):
    if not request.user.user_type == 5:
        return HttpResponse('You are not allow to view this page')
    else:
        if request.method == 'POST':
            form = PayrollManagerForm(request.POST or None)
            if form.is_valid():
                form.save()
                print('successfully')
        else:
            form = PayrollManagerForm()        
        context = {
            'form': form,
        }    
        return render(request, 'payroll/payroll_manager.html',context)

# views for upload payroll_manager files /
def payroll_manager_upload(request):
    if not request.user.user_type == 5:
        return HttpResponse('You are not allow to view this page')
    else:
        if request.method == 'POST':
            formfile = PayrollManagerUploadForm(request.POST or None, request.FILES or None)    
            # director = Director.objects.get(user=request.user.id)
            # employee = Employee.objects.get(director=director).exists()

            if formfile.is_valid():
                formfile.save()
                print('successfully')
                formfile = PayrollManagerUploadForm() 
                obj_xlsx = PayrollManagerUpload.objects.get(activated=False)
                with open(obj_xlsx.file_name.path, 'r') as f:
                    reader = xlsxwriter.Workbook(formfile)
                    worksheet = reader.add_worksheet()

                    for i, row in enumerate(worksheet):
                        if i == 0:
                            pass
                        else:
                            row = " ".join(row)
                            print(row)
        else:
            formfile = PayrollManagerUploadForm()                   
        context = {
           'formfile': formfile
        }    
        return render(request, 'payroll/payroll_manager_file.html',context)                    


'''search for leave '''



'''     
==================================================         
Admin control by directors 

views that render template for adding admin 
=====================================================

'''

'''
ADMIN LEAVE FUNCTIONALITY

'''

'''search for leave '''


def admin_search_leave(request):
    if not request.user.user_type == 5:
        return HttpResponse('You are not allow to view this page')
    else:
        if 'keyword' in request.GET:
            keyword = request.GET['keyword']
            if keyword:
                leaves = LeaveReportAdmin.objects.order_by('-created_at').filter(Q(admin__user__first_name__icontains=keyword) | Q(
                    leave_reason__icontains=keyword) | Q(admin__user__last_name__icontains=keyword))
                paginator = Paginator(leaves, 25)
                page = request.GET.get('page')
                paged_leaves = paginator.get_page(page)
                total = leaves.count()

            context = {
                'leaves': paged_leaves,
                'total': total,

            }
        return render(request, 'managements/director_template/admin_leave_view.html', context)


def admin_leave_view(request):
    if not request.user.user_type == 5:
        return HttpResponse('You are not allow to view this page')
    else:
        leaves = LeaveReportAdmin.objects.order_by('-created_at')

        paginator = Paginator(leaves, 25)
        page = request.GET.get('page')
        paged_leaves = paginator.get_page(page)
        context = {
            'leaves': paged_leaves,


        }
        return render(request, 'managements/director_template/admin_leave_view.html', context)


def admin_approve_leave(request, leave_id):
    if not request.user.user_type == 5:
        return HttpResponse('You are not allow to view this page')
    else:
        leave = LeaveReportAdmin.objects.get(id=leave_id)
        leave.leave_status = 1

        leave.save()

    return redirect('admin_leave_view')


def admin_disapprove_leave(request, leave_id):
    if not request.user.user_type == 5:
        return HttpResponse('You are not allow to view this page')
    else:
        leave = LeaveReportAdmin.objects.get(id=leave_id)
        leave.leave_status = 2
        leave.save()
        return redirect('admin_leave_view')


'''
END ADMIN LEAVE FUNCTIONALITY

'''

'''
ADMIN FEEDBACK FUNCTIONALITY

'''


def admin_feedback_message(request):
    if not request.user.user_type == 5:
        return HttpResponse('You are not allow to view this page')
    else:
        feedbacks = FeedBackAdmin.objects.all().order_by('-created_at')

        paginator = Paginator(feedbacks, 25)
        page = request.GET.get('page')
        paged_feedbacks = paginator.get_page(page)
        context = {
            'feedbacks': paged_feedbacks,

        }
        return render(request, 'managements/director_template/admin_feedback.html', context)


def admin_search_feedback(request):
    if not request.user.user_type == 5:
        return HttpResponse('You are not allow to view this page')
    else:
        if 'keywords' in request.GET:
            keywords = request.GET['keywords']
            if keywords:
                feedbacks = FeedBackAdmin.objects.all().order_by('-created_at').filter(Q(admin__user__first_name__icontains=keywords) |
                                                                                       Q(feedback__icontains=keywords) | Q(admin__user__last_name__icontains=keywords) | Q(feedback_reply__icontains=keywords))

                paginator = Paginator(feedbacks, 25)
                page = request.GET.get('page')
                paged_feedbacks = paginator.get_page(page)
                total = feedbacks.count()

            context = {
                'total': total,
                'feedbacks': paged_feedbacks,

            }

        return render(request, 'managements/director_template/admin_feedback.html', context)


@csrf_exempt
def admin_feedback_message_replied(request):
    if not request.user.user_type == 5:
        return HttpResponse('You are not allow to view this page')
    else:

        feedback_id = request.POST.get('id')
        feedback_reply = request.POST.get('message')

        try:
            feedbackadmin = FeedBackAdmin.objects.get(id=feedback_id)

            feedbackadmin.feedback_reply = feedback_reply
            feedbackadmin.save()
            return HttpResponse('True')
        except:
            return HttpResponse('False')


'''
END ADMIN FEEDBACK FUCTIONALITY

'''

'''
ADMIN NOTIFICATIONS

'''

# Notification


def director_send_notification_admin(request):
    if not request.user.user_type == 5:
        return HttpResponse('You are not allow to view this page')
    else:
        admins = Admin.objects.all()

        paginator = Paginator(admins, 2)
        page = request.GET.get('page')
        paged_admins = paginator.get_page(page)
        context = {
            'admins': paged_admins,

        }
        return render(request, 'managements/director_template/admin_notification.html', context)


def admin_search_notify(request):
    if not request.user.user_type == 5:
        return HttpResponse('You are not allow to view this page')
    else:
        if 'keywords' in request.GET:
            keywords = request.GET['keywords']
            if keywords:
                admins = Admin.objects.order_by('-date_employed').filter(Q(user__first_name__icontains=keywords) | Q(
                    user__last_name__icontains=keywords) | Q(user__other_name__icontains=keywords))

                paginator = Paginator(admins, 25)
                page = request.GET.get('page')
                paged_admins = paginator.get_page(page)
                total = admins.count()

            context = {
                'admins': paged_admins,
                'total': total,

            }

        return render(request, 'managements/director_template/admin_notification.html', context)


@csrf_exempt
def send_admin_notification(request):
    if not request.user.user_type == 5:
        return HttpResponse('You are not allow to view this page')
    else:

        id = request.POST.get("id")
        message = request.POST.get("message")
        admin = get_object_or_404(Admin, user=id)
        token = admin.fcm_token
        url = "https://fcm.googleapis.com/fcm/send"
        body = {
            "notification": {
                "title": "Cylic Payroll Management System",
                "body": message,
                "click_action": "https://cyclicpms.herokuapp.com/managements/admin_all_notificaton",
                "icon": "https://payrollmgt-bucket.s3.amazonaws.com/static/media/20200804_150827.jpg"
            },
            "to": token
        }
        headers = {
            "Content-Type": "application/json",
            "Authorization": "key=config(key)"

        }
        data = requests.post(url, data=json.dumps(body), headers=headers)

        # now saving the notification data into the table

        notification = NotificationAdmin(admin_id=admin, message=message)
        notification.save()
        # print(data.text)
        return HttpResponse("True")


'''
END ADMIN NOTIFICATIONS

'''

# search query for admin


def search_admin(request):
    if not request.user.user_type == 5:
        return HttpResponse('You are not allow to view this page')
    else:
        if 'keywords' in request.GET:
            keyword = request.GET['keywords']
            if keyword:
                admins = Admin.objects.order_by('-date_employed').filter(Q(user__first_name__icontains=keyword) | Q(
                    user__last_name__icontains=keyword) | Q(admin_unique_id__iexact=keyword))
                paginator = Paginator(admins, 25)
                page = request.GET.get('page')
                paged_admins = paginator.get_page(page)
                total = admins.count()

            context = {
                'admins': paged_admins,
                'total': total,

            }
        return render(request, 'managements/director_template/manage_admin.html', context)


# adding admin
def add_admin(request):
    if not request.user.user_type == 5:
        return HttpResponse('You are not allow to view this page')
    else:

        context = {

        }
        return render(request, 'managements/director_template/add_admin.html', context)


# views that save admin
def add_admin_save(request):
    if not request.user.user_type == 5:
        return HttpResponse('You are not allow to view this page')
    else:
        if request.method != 'POST':

            return HttpResponse('method not allowed')

        else:
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            other_name = request.POST['other_name']
            username = request.POST['username']
            email = request.POST['email']
            password = request.POST['password']
            phone_number = request.POST['phone_number']
            phone_number_2 = request.POST['phone_number_2']
            contact_address = request.POST['contact_address']
            dob = request.POST['dob']
            contact_address = request.POST['contact_address']
            gender = request.POST['gender']

            # saving it to the user database
            user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name,
                                            other_name=other_name, email=email, password=password, phone_number=phone_number, user_type=2)

            # saving it to the admin database
            user.admin.phone_number_2 = phone_number_2
            user.admin.dob = dob
            user.admin.contact_address = contact_address
            user.admin.gender = gender

            user.save()

            messages.success(request, first_name +
                             last_name + ' added successfully')
            return redirect('manage_admin')


# manage admin
def manage_admin(request):
    if not request.user.user_type == 5:
        return HttpResponse('You are not allow to view this page')
    else:
        admins = Admin.objects.order_by('-date_employed')

        # page paginator

        paginator = Paginator(admins, 25)
        page = request.GET.get('page')
        paged_admins = paginator.get_page(page)

        context = {
            'admins': paged_admins,
        }
        return render(request, 'managements/director_template/manage_admin.html', context)


# editing admin
def edit_admin(request, admin_id):
    if not request.user.user_type == 5:
        return HttpResponse('You are not allow to view this page')
    else:
        admin = Admin.objects.get(user_id=admin_id)

        context = {
            'admin': admin,
            'id': admin_id,

        }
        return render(request, 'managements/director_template/edit_admin.html', context)


def edit_admin_save(request):
    if not request.user.user_type == 5:
        return HttpResponse('You are not allow to view this page')
    else:
        if request.method != 'POST':
            messages.error(request, 'method not allowed')
            return redirect('edit-admin')

        else:
            admin_id = request.POST['admin_id']
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            other_name = request.POST['other_name']
            email = request.POST['email']
            username = request.POST['username']
            contact_address = request.POST['contact_address']
            phone_number = request.POST['phone_number']
            phone_number_2 = request.POST['phone_number_2']
            # department          = request.POST['department']

            try:
                user = User.objects.get(id=admin_id)
                user.first_name = first_name
                user.last_name = last_name
                user.other_name = other_name
                user.email = email
                user.username = username
                user.phone_number = phone_number
                user.save()

                # admin model to save

                admin = Admin.objects.get(user=admin_id)
                admin.phone_number_2 = phone_number_2
                admin.contact_address = contact_address
                # admin.department             = department
                admin.save()
                messages.success(request, 'Changes made successfully')
                return redirect('manage_admin')

            except:
                messages.error(request, 'failed to edit')
                return redirect('edit_admin')


def delete_admin(request, admin_id):
    if not request.user.user_type == 5:
        return HttpResponse('You are not allow to view this page')
    else:
        user = User.objects.get(id=admin_id)

        if request.method == 'POST':
            user.delete()
            messages.success(request, 'User deleted successfully')
            return redirect('manage_admin')

        context = {
            'user': admin_id,

        }
        return render(request, 'managements/director_template/delete_admin.html', context)
