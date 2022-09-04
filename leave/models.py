import imp
from django.db import models
from django.shortcuts import reverse
from django.utils.translation import gettext_lazy as _
# import pandas as pd
# import numpy as np

# Create your models here.
from managements.models import Admin, Employee

'''
EMPLOYEE MANAGEMENT
'''

class LeaveReportEmployee(models.Model):
    
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    # leave_date = models.CharField(max_length=100)
    leave_reason = models.TextField()
    leave_start = models.DateTimeField()
    leave_end = models.DateTimeField()
    total_days = models.CharField(max_length=100)
    leave_status = models.IntegerField(default = 0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Leave Report Employee")
        verbose_name_plural = _("Leave Report Employees")

    def __str__(self):
        return f'{self.employee.user.first_name} {self.employee.user.last_name} {self.employee.user.other_name}'

    def get_absolute_url(self):
        return reverse("leavereportemployee-detail", kwargs={"pk": self.pk})
    
    def save(self,*args, **kwargs):
        self.total_days = 0
        leave_end = pd.to_datetime(self.leave_end).date()
        leave_start = pd.to_datetime(self.leave_start).date()
        self.total_days = np.busday_count(leave_start, leave_end, holidays=[leave_start, leave_end])
        
        super(LeaveReportEmployee,self).save(*args, **kwargs)


class FeedBackEmployee(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    feedback = models.TextField()
    feedback_reply = models.TextField(blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Feed Back Employee")
        verbose_name_plural = _("Feed Back Employees")

    def __str__(self):
        return f'{self.employee.user.first_name} {self.employee.user.last_name} {self.employee.user.other_name}'

    def get_absolute_url(self):
        return reverse("feedbackemployee_detail", kwargs={"pk": self.pk})
    
class NotificationEmployee(models.Model):
    employee_id = models.ForeignKey(Employee,on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField( auto_now_add=True)
    updated_at = models.DateTimeField( auto_now=True)
    objects = models.Manager()

    class Meta:
        verbose_name = _("Notification Employee")
        verbose_name_plural = _("Notification Employees")


    def __str__(self):
        return f'{self.employee_id.user.first_name} {self.employee_id.user.last_name} {self.employee_id.user.other_name}'

'''
END EMPLOYEE MANAGEMENT
'''


'''
ADMIN MANAGEMENT
'''


class LeaveReportAdmin(models.Model):
    
    admin = models.ForeignKey(Admin, on_delete=models.CASCADE)
    leave_date = models.CharField(max_length=100)
    leave_reason = models.TextField()
    leave_start = models.DateTimeField()
    leave_end = models.DateTimeField()
    leave_status = models.IntegerField(default = 0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Leave Report Admin")
        verbose_name_plural = _("Leave Report Admins")

    def __str__(self):
        return f'{self.admin.user.first_name} {self.admin.user.last_name} {self.admin.user.other_name}'

    def get_absolute_url(self):
        return reverse("leavereportadmin-detail", kwargs={"pk": self.pk})
    
class FeedBackAdmin(models.Model):
    
    admin = models.ForeignKey(Admin, on_delete=models.CASCADE)
    feedback = models.TextField()
    feedback_reply = models.TextField(blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _("Feed Back Admin")
        verbose_name_plural = _("Feed Back Admins")

    def __str__(self):
        return f'{self.admin.user.first_name} {self.admin.user.last_name} {self.admin.user.other_name}'

    def get_absolute_url(self):
        return reverse("feedbackadmin_detail", kwargs={"pk": self.pk})
    
class NotificationAdmin(models.Model):
    admin_id = models.ForeignKey(Admin,on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField( auto_now_add=True)
    updated_at = models.DateTimeField( auto_now_add=True)
    objects = models.Manager()

    class Meta:
        verbose_name = _("Notification Admin")
        verbose_name_plural = _("Notification Admins")


    def __str__(self):
        return f'{self.admin_id.user.first_name} {self.admin_id.user.last_name} {self.admin_id.user.other_name}'


'''
END ADMIN MANAGEMENT
'''