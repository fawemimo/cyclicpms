from email.policy import default
import imp
from django.db import models
from django.shortcuts import reverse
from django.utils.translation import gettext_lazy as _
import pandas as pd
import numpy as np
from django.contrib import messages
# Create your models here.
from managements.models import Admin, Employee

"""
EMPLOYEE MANAGEMENT
"""


class LeaveReportEmployee(models.Model):
    """
    DB for employee to applied or request for leave
    """

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    leave_reason = models.TextField()
    leave_start = models.DateTimeField()
    leave_end = models.DateTimeField()
    total_duration_days = models.CharField(max_length=100, blank=True,null=True)
    total_days_left = models.CharField(max_length=255, blank=True, null=True)
    leave_comment = models.CharField(max_length=255, blank=True)
    leave_status = models.IntegerField(default=0)
    is_on_leave = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Leave Report Employee")
        verbose_name_plural = _("Leave Report Employees")

    def __str__(self):
        return f"{self.employee.user.first_name} {self.employee.user.last_name} {self.employee.user.other_name}"

    def get_absolute_url(self):
        return reverse("leavereportemployee-detail", kwargs={"pk": self.pk})

    def save(self, *args, **kwargs):
        self.total_duration_days = 0
        # set the leave_allocation_days
        self.employee.leave_allocation_days = 0

        # set the total_duration_days
        self.total_duration_days = 0

        # compare the leave days
        if self.employee.leave_allocation_days > self.total_duration_days:
            messages.error(self,'Number of allocation days exceed')
        leave_end = pd.to_datetime(self.leave_end).date()
        leave_start = pd.to_datetime(self.leave_start).date()
        self.total_duration_days = np.busday_count(leave_start, leave_end, holidays=[leave_start, leave_end])

       
        if self.leave_status == 1 :
            self.is_on_leave = True   
        super(LeaveReportEmployee, self).save(*args, **kwargs)


class FeedBackEmployee(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    feedback = models.TextField()
    feedback_reply = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Feed Back Employee")
        verbose_name_plural = _("Feed Back Employees")

    def __str__(self):
        return f"{self.employee.user.first_name} {self.employee.user.last_name} {self.employee.user.other_name}"

    def get_absolute_url(self):
        return reverse("feedbackemployee_detail", kwargs={"pk": self.pk})


class NotificationEmployee(models.Model):
    employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()

    class Meta:
        verbose_name = _("Notification Employee")
        verbose_name_plural = _("Notification Employees")

    def __str__(self):
        return (
            f"{self.employee_id.user.first_name} {self.employee_id.user.last_name} {self.employee_id.user.other_name}"
        )


"""
END EMPLOYEE MANAGEMENT
"""


"""
ADMIN MANAGEMENT
"""


class LeaveReportAdmin(models.Model):

    admin = models.ForeignKey(Admin, on_delete=models.CASCADE)
    leave_date = models.CharField(max_length=100)
    leave_reason = models.TextField()
    leave_start = models.DateTimeField()
    leave_end = models.DateTimeField()
    leave_status = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Leave Report Admin")
        verbose_name_plural = _("Leave Report Admins")

    def __str__(self):
        return f"{self.admin.user.first_name} {self.admin.user.last_name} {self.admin.user.other_name}"

    def get_absolute_url(self):
        return reverse("leavereportadmin-detail", kwargs={"pk": self.pk})


class FeedBackAdmin(models.Model):

    admin = models.ForeignKey(Admin, on_delete=models.CASCADE)
    feedback = models.TextField()
    feedback_reply = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _("Feed Back Admin")
        verbose_name_plural = _("Feed Back Admins")

    def __str__(self):
        return f"{self.admin.user.first_name} {self.admin.user.last_name} {self.admin.user.other_name}"

    def get_absolute_url(self):
        return reverse("feedbackadmin_detail", kwargs={"pk": self.pk})


class NotificationAdmin(models.Model):
    admin_id = models.ForeignKey(Admin, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()

    class Meta:
        verbose_name = _("Notification Admin")
        verbose_name_plural = _("Notification Admins")

    def __str__(self):
        return f"{self.admin_id.user.first_name} {self.admin_id.user.last_name} {self.admin_id.user.other_name}"


"""
END ADMIN MANAGEMENT
"""
