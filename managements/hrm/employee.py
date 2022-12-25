from django.http import HttpResponse, JsonResponse
from directors.models import Director
from accounts.models import User
from django.shortcuts import get_object_or_404, redirect, render, reverse
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from managements.hrm.forms import DepartmentForm
from payroll.forms import PayrollManagerForm, PayrollManagerUploadForm
from payroll.models import *
import csv
from managements.forms import *
from managements.hrm.forms import *
from managements.models import *
from django.core.paginator import Paginator


def add_employee(request):
    """ 
    HRM TO ADD/CREATE EMPLOYEE'S
    """
    if not request.user.user_type == 5:
        return HttpResponse("You are not allow to view this page")
    else:
        directors = Director.objects.get(user=request.user.id)
        context = {
            "directors": directors,
        }
        return render(request, "managements/director_template/add_employee.html", context)


def add_employee_save(request):
    """ 
    SINGLE CREATION OF EMPLOYEE's
    """
    if not request.user.user_type == 5:
        return HttpResponse("You are not allow to view this page")
    else:
        if request.method != "POST":
            return HttpResponse("method not allowed")
        else:
            fs = FileSystemStorage()
            director = request.POST.get("director")
            first_name = request.POST["first_name"]
            last_name = request.POST["last_name"]
            other_name = request.POST["other_name"]
            username = request.POST["username"]
            email = request.POST["email"]
            password = request.POST["password"]
            phone_number = request.POST["phone_number"]

            """
            profile_pic         = request.FILES.get('profile_pic')
            profile_pic_path    = fs.save(profile_pic.name,profile_pic)
            profile_pic_url     = fs.url(profile_pic_path)
            """
            # saving user data
            user = User.objects.create_user(
                username=username,
                first_name=first_name,
                last_name=last_name,
                other_name=other_name,
                email=email,
                password=password,
                phone_number=phone_number,
                user_type=1,
            )
            director_obj = Director.objects.get(user=director)
            user.employee.director = director_obj
            # user.employee.profile_pic       = profile_pic_url
            user.save()

            messages.success(request, first_name + last_name + " added successfully")
            # changing the redirecting to add category later
            return redirect("manage-employee")


def add_upload_employee(request):

    """
    BULK CREATION OF EMPLOYEEs
    """
    if request.user.user_type != 5:
        return HttpResponse("You are not allow to view this page")
    else:
        if request.method == "POST":
            directors = Director.objects.get(user=request.user.id)
            employees = Employee.objects.filter(director=directors).order_by("-date_employed").exists()

            form = UploadEmployeeForm(request.POST or None, request.FILES or None)
            if form.is_valid():
                if employees:
                    messages.error(request, "User already exists")
                    return redirect("add-employee")
                # if (str(form).split('.')[-1] == 'csv'):
                #     print('success')
                # else:
                #     messages.error(request, 'Invalid file format: file must be a CSV format')
                #     return redirect('add-employee')

                form.save()

                form = UploadEmployeeForm()
                obj_csv = UploadEmployee.objects.get(activated=False)
                with open(obj_csv.file_name.path, "r") as f:
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
                            director_obj = Director.objects.get(user=request.user.id)

                            user = User.objects.create_user(
                                username=username,
                                email=email,
                                first_name=first_name,
                                last_name=last_name,
                                other_name=other_name,
                                password=password,
                                phone_number=phone_number,
                                user_type=1,
                            )

                            user.employee.director = director_obj
                            user.save()
                            print(
                                first_name,
                                last_name,
                                other_name,
                                username,
                                email,
                                password,
                                phone_number,
                                director_obj,
                            )
                    obj_csv.activated = True
                    obj_csv.save()
                return redirect("manage-employee")
        return render(request, "managements/director_template/add_employee.html", {"form": form})


def manage_employee(request):

    """
    RETRIEVING EMPLOYEE TO MANAGE
    """

    if not request.user.user_type == 5:
        return HttpResponse("You are not allow to view this page")
    else:

        directors = Director.objects.get(user=request.user.id)
        employees = Employee.objects.filter(director=directors).order_by("-date_employed")

        paginator = Paginator(employees, 25)
        page = request.GET.get("page")
        paged_employees = paginator.get_page(page)

        context = {
            "employees": paged_employees,
            "directors": directors,
        }

    return render(request, "managements/director_template/manage_employee.html", context)



def edit_employee(request, employee_id):
    """ 
    UPDATING EMPLOYEE
    """
    if not request.user.user_type == 5:
        return HttpResponse("You are not allow to view this page")
    else:
        # x_forwarded_for = request.META.get("HTTP_USER_AGENT")
        # if x_forwarded_for:
        #     ip = x_forwarded_for.split(",")[0]
        #     print(f"This is the IP {ip}")
        # else:
        #     ip = request.META.get("HTTP_USER_AGENT")
        #     print(f"Else this is the IP {ip}")

        # get the director user request
        director = Director.objects.get(user=request.user.id)

        # get the list of departmet created by the director
        department = Department.objects.filter(director=director).distinct()

        # get the employee each details
        employee = Employee.objects.get(user_id=employee_id)

        # get the employee data set
        employee_data = EmployeeData.objects.get(employee__user=employee.user)

        # get the employee salary details monthly        
        salary_attribute = SalaryAttributeValues.objects.filter(employee_data__employee=employee)

        # get the total breakdown of each employee
        salary_breakdown = SalaryAttributeValue.objects.filter(director=director)

        # get the total deductions breakdown of each employee
        deduction_breakdown = DeductionAttributeValue.objects.filter(director=director)
        for x in deduction_breakdown:
            print(x.deduction_attribute.name)

        # get the deductions details mothly
        deduction_attribute = DeductionAttributeValues.objects.filter(employee_data__employee=employee)

        # get the employee pay role modules
        job_role = JobRole.objects.filter(director=director)
        pay_group = PayGroup.objects.filter(director=director)
        pay_grade = PayGrade.objects.filter(director=director)
        for x in job_role:
            print(x.name)

        # get the actual employee roles
        employee_role = EmployeeRole.objects.get(employee=employee)
        context = {
            "employee": employee,
            "id": employee_id,
            "department": department,
            "employee_data":employee_data,
            "salary_attribute":salary_attribute,
            "deduction_attribute":deduction_attribute,
            "deduction_breakdown":deduction_breakdown,
            "salary_breakdown":salary_breakdown,
            "job_role":job_role,
            "pay_group":pay_group,
            "pay_grade":pay_grade
        }
        return render(request, "managements/director_template/edit_employee.html", context)


# @login_required
def edit_employee_save(request):
    if not request.user.user_type == 5:
        return HttpResponse("You are not allow to view this page")
    else:
        if request.method != "POST":
            messages.error(request, "method not allowed")
            return redirect("edit-employee")

        else:
            # profile_pic         = request.FILES.get('profile_pic')
            employee_id = request.POST["employee_id"]
            first_name = request.POST["first_name"]
            last_name = request.POST["last_name"]
            other_name = request.POST["other_name"]
            email = request.POST["email"]
            username = request.POST["username"]
            contact_address = request.POST["contact_address"]
            phone_number = request.POST["phone_number"]
            phone_number_2 = request.POST["phone_number_2"]

            # Employee Role
            is_manager = request.POST['is_manager']
            is_supervisor = request.POST['is_supervisor']

            # PAY ROLE
            job_role = request.POST['job_role']
            pay_grade = request.POST['pay_grade']

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

                # EMPLOYEE ROLE MODEL TO SAVE
                employee_role = EmployeeRole.objects.get(employee=employee_id)
                employee_role.is_manager  = is_manager
                employee_role.is_supervisor = is_supervisor
                print(employee_role.is_manager)
                employee_role.save()

                # ROLE MODEL TO SAVE
                jobrole = JobRole.objects.get(director=employee.director)
                jobrole.name = job_role
                jobrole.save()

                paygrade = PayGrade.objects.get(director=employee.director)
                paygrade.job_role = jobrole
                paygrade.name = pay_grade
                paygrade.save()

                messages.success(request, "Changes made successfully")
                return redirect("manage-employee")

            except:
                messages.error(request, "failed to edit")
                return redirect("manage-employee")


def delete_employee(request, employee_id):
    """ 
    DELETING EMPLOYEE
    """
    if not request.user.user_type == 5:
        return HttpResponse("You are not allow to view this page")
    else:
        name = request.GET.get("name")

        directors = Director.objects.get(user=request.user.id)
        user = User.objects.get(id=employee_id)

        if request.method == "POST":
            user.delete()
            messages.success(request, "User deleted successfully")
            return redirect("manage-employee")

        context = {"user": employee_id, "directors": directors}
        return render(request, "managements/director_template/delete_user.html", context)


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
