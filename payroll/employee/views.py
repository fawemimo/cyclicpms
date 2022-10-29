# from accounts.models import Profile
from django.shortcuts import render
from django.http import HttpResponse
from managements.models import Employee
from payroll.models import DeductionAttributeValues, EmployeeData, SalaryAttributeValues
from django.db.models import Count, Sum

# Create your views here.
def payslip_data(request):
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

        # Render the data into the template
        context = {
            "employee": employee,
            "employee_data": employee_data,
            "salary_attribute": salary_attribute,
            "salary_attribute_total": salary_attribute_total,
            "deduction_attribute": deduction_attribute,
            "deduction_attribute_total": deduction_attribute_total,
            "grand_total": grand_total,
        }

        return render(request, "payroll/employee_template/payslip.html", context)


