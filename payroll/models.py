from django.db import models

from managements.models import Employee


# Payroll Manager bulk creations file in .csv, .xlsx format /
class PayrollManagerUpload(models.Model):
    file_name = models.FileField(upload_to='payroll_manager')
    activated = models.BooleanField(default=False)
    updated = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Payroll Manager Upload'
        verbose_name_plural = 'Payroll Manager Uploads'


# Payroll Manager system model /
class PayrollManager(models.Model):
    employee_number                     = models.ForeignKey(Employee, related_name='employee_unique_number', on_delete=models.DO_NOTHING)
    employee_name                       = models.ForeignKey(Employee, on_delete=models.DO_NOTHING)
    pay_group                           = models.CharField(max_length=255)
    grade                               = models.CharField(max_length=255)
    basic_pay                           = models.PositiveIntegerField(default=0)
    housing_amount                      = models.PositiveIntegerField(blank=True,null=True,default=0)
    housing_upfront                     = models.IntegerField(blank=True,null=True,default=0)
    transport_amount                    = models.IntegerField(blank=True,null=True,default=0)
    utility_amount                      = models.IntegerField(blank=True,null=True,default=0)
    passage_amount                      = models.IntegerField(blank=True,null=True,default=0)
    furniture_amount                    = models.IntegerField(blank=True,null=True,default=0)
    dressing_amount                     = models.IntegerField(blank=True,null=True,default=0)
    driver_refund                       = models.IntegerField(blank=True,null=True,default=0)
    leave_allowance                     = models.IntegerField(blank=True,null=True,default=0)
    vehicle_refund                      = models.IntegerField(blank=True,null=True,default=0)
    children_eduction_allowance         = models.IntegerField(blank=True,null=True,default=0)
    gross_pay                           = models.IntegerField(blank=True,null=True,default=0)
    paye                                = models.IntegerField(blank=True,null=True,default=0)
    loan_repayment                      = models.IntegerField(blank=True,null=True,default=0)
    NHF                                 = models.IntegerField(blank=True,null=True,default=0)
    HMO_deduction                       = models.IntegerField(blank=True,null=True,default=0)
    other_deduction                     = models.IntegerField(blank=True,null=True,default=0)
    status_car_repayment                = models.IntegerField(blank=True,null=True,default=0)
    total_deduction                     = models.IntegerField(blank=True,null=True,default=0)
    NET_PAY                             = models.IntegerField(blank=True,null=True,default=0)

    def __str__(self):
        return self.employee_name.user.first_name

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Payroll Manager'
        verbose_name_plural = 'Payroll Managers' 