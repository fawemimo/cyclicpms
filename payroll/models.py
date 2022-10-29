from django.db import models
from directors.models import *

from managements.models import Employee
from set_salary.models import DeductionAttributeValue, SalaryAttributeValue


# Payroll Manager bulk creations file in .csv, .xlsx format /
class PayrollManagerUpload(models.Model):
    file_name = models.FileField(upload_to="payroll_manager")
    activated = models.BooleanField(default=False)
    updated = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)

    class Meta:
        db_table = ""
        managed = True
        verbose_name = "Payroll Manager Upload"
        verbose_name_plural = "Payroll Manager Uploads"


# Payroll Manager system model /
class PayrollManager(models.Model):
    employee_number = models.ForeignKey(Employee, related_name="employee_unique_number", on_delete=models.DO_NOTHING)
    employee_name = models.ForeignKey(Employee, on_delete=models.DO_NOTHING)
    pay_group = models.CharField(max_length=255)
    grade = models.CharField(max_length=255)
    basic_pay = models.PositiveIntegerField(default=0)
    housing_amount = models.PositiveIntegerField(blank=True, null=True, default=0)
    housing_upfront = models.IntegerField(blank=True, null=True, default=0)
    transport_amount = models.IntegerField(blank=True, null=True, default=0)
    utility_amount = models.IntegerField(blank=True, null=True, default=0)
    passage_amount = models.IntegerField(blank=True, null=True, default=0)
    furniture_amount = models.IntegerField(blank=True, null=True, default=0)
    dressing_amount = models.IntegerField(blank=True, null=True, default=0)
    driver_refund = models.IntegerField(blank=True, null=True, default=0)
    leave_allowance = models.IntegerField(blank=True, null=True, default=0)
    vehicle_refund = models.IntegerField(blank=True, null=True, default=0)
    children_eduction_allowance = models.IntegerField(blank=True, null=True, default=0)
    gross_pay = models.IntegerField(blank=True, null=True, default=0)
    paye = models.IntegerField(blank=True, null=True, default=0)
    loan_repayment = models.IntegerField(blank=True, null=True, default=0)
    NHF = models.IntegerField(blank=True, null=True, default=0)
    HMO_deduction = models.IntegerField(blank=True, null=True, default=0)
    other_deduction = models.IntegerField(blank=True, null=True, default=0)
    status_car_repayment = models.IntegerField(blank=True, null=True, default=0)
    total_deduction = models.IntegerField(blank=True, null=True, default=0)
    NET_PAY = models.IntegerField(blank=True, null=True, default=0)

    def __str__(self):
        return self.employee_name.user.first_name

    class Meta:
        db_table = ""
        managed = True
        verbose_name = "Payroll Manager"
        verbose_name_plural = "Payroll Managers"


class JobRole(models.Model):
    """
    Adding Job roles to employee
    """
    director = models.ForeignKey(Director,on_delete=models.DO_NOTHING, blank=True,null=True)
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Job Role"
        verbose_name_plural = "Job Roles"


class PayGrade(models.Model):
    """
    Adding different Pay group to employees
    """
    director = models.ForeignKey(Director,on_delete=models.DO_NOTHING, blank=True,null=True)
    job_role = models.OneToOneField(JobRole, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Pay Grade"
        verbose_name_plural = "Pay Grades"


class PayGroup(models.Model):
    """'
    Adding Pay Group to employees
    """
    director = models.ForeignKey(Director,on_delete=models.DO_NOTHING, blank=True,null=True)
    pay_grade = models.OneToOneField(PayGrade, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Pay Group"
        verbose_name_plural = "Pay Groups"


class DeductionAttributeValues(models.Model):
    """
    Deduction Attribute relating link table to Deduction Attribute Value
    """
    director = models.ForeignKey(Director,on_delete=models.DO_NOTHING, blank=True,null=True)
    deduction_attribute_value = models.OneToOneField(
        DeductionAttributeValue, on_delete=models.CASCADE, related_name="salaryattributevaluess"
    )
    employee_data = models.ForeignKey("EmployeeData", on_delete=models.CASCADE, related_name="employee_data")

    def __str__(self):
        return f"{self.deduction_attribute_value}"

    class Meta:
        db_table = ""
        managed = True
        verbose_name = "DeductionAttributeValues"
        verbose_name_plural = "DeductionAttributeValuess"


class EmployeeData(models.Model):

    """
    Model showing the collectives data of employee
    """

    employee = models.OneToOneField(Employee, on_delete=models.PROTECT)
    job_role = models.ForeignKey(JobRole, on_delete=models.DO_NOTHING)
    pay_grade = models.ForeignKey(PayGrade, on_delete=models.DO_NOTHING)
    pay_group = models.ForeignKey(PayGroup, on_delete=models.DO_NOTHING)
    salary_attribute_value = models.ManyToManyField(
        SalaryAttributeValue,
        related_name="salary_attribute_values",
        through="SalaryAttributeValues",
    )
    deduction_attribute_value = models.ManyToManyField(
        DeductionAttributeValue, related_name="DeductionAttributeValue", through="DeductionAttributeValues",
    )

    def __str__(self):
        return f"{self.employee.user.first_name}"

    class Meta:
        verbose_name = "EmployeeData"
        verbose_name_plural = "EmployeeDatas"


class SalaryAttributeValues(models.Model):
    """
    Relating both Salary Attribute and Salary Value Link Table
    """
    director = models.ForeignKey(Director,on_delete=models.DO_NOTHING, blank=True,null=True)
    salary_attribute_value = models.OneToOneField(
        SalaryAttributeValue, on_delete=models.CASCADE, related_name="salaryattributevaluess"
    )
    employee_data = models.ForeignKey(EmployeeData, on_delete=models.CASCADE, related_name="employeedata")

    def __str__(self):
        return f"{self.salary_attribute_value}"

    class Meta:
        verbose_name = "SalaryAttributeValues"
        verbose_name_plural = "SalaryAttributeValuess"
        unique_together = (("salary_attribute_value", "employee_data"),)
