from django.http import HttpResponse, JsonResponse
from directors.models import Director
from accounts.models import User
from django.shortcuts import get_object_or_404, redirect, render, reverse
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from payroll.forms import PayrollManagerForm, PayrollManagerUploadForm
from payroll.models import PayrollManagerUpload
import csv
from managements.forms import *
from managements.models import *
from django.core.paginator import Paginator

""" 
HRM TO ADD/CREATE EMPLOYEE'S
"""
def add_employee(request):
    if not request.user.user_type == 5:
        return HttpResponse('You are not allow to view this page')
    else:
        
        directors = Director.objects.get(user=request.user.id)

        context = {
            'directors': directors
        }
        return render(request, 'managements/director_template/add_employee.html', context)

""" 
SINGLE CREATION OF EMPLOYEE's
"""
def add_employee_save(request):
    if not request.user.user_type == 5:
        return HttpResponse('You are not allow to view this page')
    else:
        if request.method != 'POST':

            return HttpResponse('method not allowed')

        else:
            fs = FileSystemStorage()
            director = request.POST.get('director')
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            other_name = request.POST['other_name']
            username = request.POST['username']
            email = request.POST['email']
            password = request.POST['password']
            phone_number = request.POST['phone_number']

            """
            # phone_number_2      = request.POST['phone_number_2']
            # contact_address     = request.POST['contact_address']
            # dob                 = request.POST['dob']
            # contact_address     = request.POST['contact_address']
            # gender              = request.POST['gender']
            # profile_pic         = request.FILES.get('profile_pic')

            # profile_pic_path    = fs.save(profile_pic.name,profile_pic)
            # profile_pic_url     = fs.url(profile_pic_path)
            # try: 
            
            """
            # saving user data 
            user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name,
                                            other_name=other_name, email=email, password=password, phone_number=phone_number, user_type=1)
            director_obj = Director.objects.get(user=director)

            """ # creating the models for employees

            # user.employee.phone_number_2    = phone_number_2
            # user.employee.dob               = dob
            # user.employee.contact_address   = contact_address
            # user.employee.gender            = gender """
            user.employee.director = director_obj
            # user.employee.profile_pic       = profile_pic_url

            user.save()

            messages.success(request, first_name +
                             last_name + ' added successfully')
            # changing the redirecting to add category later
            return redirect('manage-employee')
            # except:
            #     print('failed')


""" 
BULK CREATION OF EMPLOYEEs
"""

def add_upload_employee(request):
    if not request.user.user_type == 5:
        return HttpResponse('You are not allow to view this page')
    else:
        if request.method == 'POST':            
            directors = Director.objects.get(user=request.user.id)
            employees = Employee.objects.filter(
            director=directors).order_by('-date_employed').exists()
            
            form = UploadEmployeeForm(
                request.POST or None, request.FILES or None)                
            if form.is_valid():   
                if employees:
                    messages.error(request, 'User already exists')
                    return redirect('add-employee')      
                # if (str(form).split('.')[-1] == 'csv'):
                #     print('success')                    
                # else:
                #     messages.error(request, 'Invalid file format: file must be a CSV format')
                #     return redirect('add-employee')
       
                form.save()
               
                form = UploadEmployeeForm()
                obj_csv = UploadEmployee.objects.get(activated=False)
                with open(obj_csv.file_name.path, 'r') as f:
                    reader = csv.reader(f)

                    for i, row in enumerate(reader):
                        if i == 0:
                            pass
                        else:
                            row = " ".join(row)
                            row = row.replace(";", " ")
                            row = row.split()
                            print(row)
                            print(type(row))
                            first_name = row[0]
                            last_name = row[1]
                            other_name = row[2]
                            username = row[3]
                            email = row[4]
                            password = row[5]
                            phone_number = int(row[6])
                            director_obj = Director.objects.get(
                                user=request.user.id)

                            user = User.objects.create_user(username=username, email=email, first_name=first_name, last_name=last_name,
                                                            other_name=other_name, password=password, phone_number=phone_number, user_type=1)

                            user.employee.director = director_obj
                            user.save()
                            print(first_name, last_name, other_name, username,
                                  email, password, phone_number, director_obj)
                    obj_csv.activated = True
                    obj_csv.save()
                return redirect('manage-employee')
        return render(request, 'managements/director_template/add_employee.html', {'form': form})


""" 
RETRIEVING EMPLOYEE TO MANAGE
"""
def manage_employee(request):
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
            'employees': paged_employees,
            'directors': directors,
        }

    return render(request, 'managements/director_template/manage_employee.html', context)

""" 
UPDATING EMPLOYEE
"""
# @login_required
def edit_employee_save(request):
    if not request.user.user_type == 5:
        return HttpResponse('You are not allow to view this page')
    else:
        if request.method != 'POST':
            messages.error(request, 'method not allowed')
            return redirect('edit-employee')

        else:
            # profile_pic         = request.FILES.get('profile_pic')
            employee_id = request.POST['employee_id']
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            other_name = request.POST['other_name']
            email = request.POST['email']
            username = request.POST['username']
            contact_address = request.POST['contact_address']
            phone_number = request.POST['phone_number']
            phone_number_2 = request.POST['phone_number_2']

            try:
                user = User.objects.get(id=employee_id)
                user.first_name = first_name
                user.last_name = last_name
                user.other_name = other_name
                user.email = email
                user.username = username
                user.phone_number = phone_number
                user.save()
                # employee model to save

                employee = Employee.objects.get(user=employee_id)
                employee.phone_number_2 = phone_number_2
                employee.contact_address = contact_address
                # employee.profile_pic                   = profile_pic
                employee.save()

                messages.success(request, 'Changes made successfully')
                return redirect('manage-employee')

            except:
                messages.error(request, 'failed to edit')
                return redirect('manage-employee')



""" 
DELETING EMPLOYEE
"""
def delete_employee(request, employee_id):
    if not request.user.user_type == 5:
        return HttpResponse('You are not allow to view this page')
    else:
        name = request.GET.get('name')

        directors = Director.objects.get(user=request.user.id)
        user = User.objects.get(id=employee_id)

        if request.method == 'POST':
            user.delete()
            messages.success(request, 'User deleted successfully')
            return redirect('manage-employee')

        context = {
            'user': employee_id,

            'directors': directors
        }
        return render(request, 'managements/director_template/delete_user.html', context)




# editing employee
def edit_employee(request, employee_id):

    if not request.user.user_type == 5:
        return HttpResponse('You are not allow to view this page')
    else:
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        employee = Employee.objects.get(user_id=employee_id)
        #

        context = {

            'employee': employee,
            'id': employee_id,
            #
        }
        print(ip)
        return render(request, 'managements/director_template/edit_employee.html', context)




""" 

def addemployee(request):

    if request.method == 'POST':
        form = UserExtendedForm(request.POST)
        employee_form = EmployeeForm(request.POST)

        if form.is_valid() and employee_form.is_valid():
            user = form.save()
            employee = employee_form.save(commit=False)
            employee.user = user

            employee.save()

            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=email, password=password)
            print('its seem good')
            return redirect('directors')

    else:
        form = UserExtendedForm()
        employee_form = EmployeeForm()

    context = {
        'form': form,
        'employee_form': employee_form
    }
    return render(request, 'managements/add_employee.html', context)
 """            