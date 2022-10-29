# from accounts.models import Profile
import datetime
from django.shortcuts import render, redirect
from django.http import HttpResponse
from accounts.models import User
from dashboards.forms import TodoForm
from directors.models import Director
from managements.models import Department, Employee, EmployeeRole
from payroll.models import DeductionAttributeValues, EmployeeData, SalaryAttributeValues
from django.db.models import Count, Sum
from django.contrib.postgres.aggregates import ArrayAgg
from django.db.models.functions import TruncMonth, Extract
import socket
import json
import urllib.request
import ipinfo
import pycountry
import requests
from urllib.request import urlopen
import re as r
import geocoder
from countryinfo import CountryInfo
import holidays
from datetime import date
from leave.models import LeaveReportEmployee
import pandas as pd
import numpy as np
from django.contrib import messages
from django.views.decorators.http import require_POST
from todo.models import Todo


def staff(request):
    if not request.user.user_type == 1:
        return HttpResponse("You are not allow to view this page")
    else:
        # Get the employee user instance
        employee = Employee.objects.get(user=request.user.id)

        # Get the employee data  instance  with employee
        employee_data = EmployeeData.objects.get(employee=employee)

        # Filter the employee salary attribute and values
        salary_attribute = SalaryAttributeValues.objects.filter(employee_data=employee_data)

        # Get the total value of the employee salary attribute values
        salary_attribute_total = SalaryAttributeValues.objects.filter(employee_data=employee_data).aggregate(
            Sum("salary_attribute_value__value")
        )["salary_attribute_value__value__sum"]

        # Get the deductions of the employee
        deduction_attribute = DeductionAttributeValues.objects.filter(employee_data=employee_data)

        # Get the total deduction attribute value of the employee
        deduction_attribute_total = DeductionAttributeValues.objects.filter(employee_data=employee_data).aggregate(
            Sum("deduction_attribute_value__attribute_value")
        )["deduction_attribute_value__attribute_value__sum"]

        # Get the grand total of the salary
        grand_total = 0
        grand_total = salary_attribute_total - deduction_attribute_total

        # get the total number of employee in your company
        all_employee = Employee.objects.all().filter(director=employee.director).exclude(user=request.user)

        # get the current year of the server time
        year = datetime.date.today().strftime("%Y")
        # iterate the calendar for holidays in a year
        holiday = holidays.Nigeria(years=int(year)).items()

        # get the supervisor of the department
        is_supervisor = (
            EmployeeRole.objects.filter(employee__director=employee.director)
            .filter(employee__department__name__iexact=employee.department.name)
            .filter(is_supervisor=True)
        )

        # get the total leave days
        leave = (
            LeaveReportEmployee.objects.filter(employee=employee)
            .annotate(total=Sum("total_duration_days"))
            .values("total_days_left")
        )

        # get the employee that is on leave
        is_on_leave = (
            LeaveReportEmployee.objects.filter(employee__director=employee.director)
            .filter(employee__department__name__iexact=employee.department.name)
            .filter(is_on_leave=True)
        )

        # get total employee(S) for monthly birthdays
        current_month = datetime.date.today().month
        birthdays = Employee.objects.all().filter(director=employee.director).filter(dob__month=current_month)

        # User Todo List
        todo_list = Todo.objects.filter(user=request.user.id).order_by("id")

        # Todo form
        todoform = TodoForm()

        # Render the data into the template
        context = {
            "employee": employee,
            "employee_data": employee_data,
            "salary_attribute": salary_attribute,
            "salary_attribute_total": salary_attribute_total,
            "deduction_attribute": deduction_attribute,
            "deduction_attribute_total": deduction_attribute_total,
            "grand_total": grand_total,
            "holidays": holiday,
            "employees": all_employee,
            "is_supervisor": is_supervisor,
            "leave": leave,
            "is_on_leave": is_on_leave,
            "birthdays": birthdays,
            "todo_list": todo_list,
            "todoform": todoform,
        }

        return render(request, "dashboards/employee_template/employee.html", context)


# Adding TODO list
def addTodo(request):
    if request.user.is_authenticated:
        if request.method != "POST":
            return HttpResponse("Method not allow")
        else:
            user = request.POST.get("user")
            description = request.POST["description"]
            try:

                user = User.objects.get(id=request.user.id)
                todo = Todo(user=user, description=description, is_completed=False)
                todo.save()
                messages.success(request, "ToDo Added Successfully")
                return redirect("employee")
            except:
                messages.error(request, "ToDo Failed To Add")
                return redirect("employee")
    else:
        return HttpResponse("Log in to add TODO")


# Showing pending todo
def pendingtodo(request):
    if request.user.is_authenticated:
        user = User.objects.get(id=request.user.id)
        pending_todo = Todo.objects.filter(user=user).filter(user=request.user.id).filter(is_completed=False)
        context = {
            "pending_todo": pending_todo,
        }

    else:
        return HttpResponse("Log in to see TODO")
    return render(request, "dashboards/employee_template/employee.html", context)


# Showing complete todo
def completetodo(request):
    if request.user.is_authenticated:
        complete_todo = Todo.objects.filter(user=request.user.id).filter(is_completed=True)
        context = {
            "complete_todo": complete_todo,
        }

    else:
        return HttpResponse("Log in to see TODO")
    return render(request, "dashboards/employee_template/employee.html", context)


# Activating is_completed
def is_completed(request, is_completed):
    if request.user.is_authenticated:
        user = User.objects.get(id=request.user.id)
        todo = Todo.objects.filter(user=user).get(pk=is_completed)
        todo.is_completed = True
        todo.save()
    return redirect("employee")


# Delete complete todo 
def deleteComplete(request):
    if request.user.is_authenticated:
        user = User.objects.get(id=request.user.id)
        todo = Todo.objects.filter(user=user).filter(is_completed__exact=True).delete()
        
    return redirect("employee")


# Delete all todo 
def alldelete(request):
    if request.user.is_authenticated:
        user = User.objects.get(id=request.user.id)
        todo = Todo.objects.filter(user=user).delete()
        
    return redirect("employee")