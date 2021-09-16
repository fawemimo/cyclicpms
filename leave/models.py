from django.db import models

# Create your models here.
from managements.models import Employee
from django.utils.translation import ugettext_lazy as _
from django.shortcuts import reverse

class LeaveReportEmployee(models.Model):
    
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    leave_date = models.CharField(max_length=100)
    leave_reason = models.TextField()
    leave_status = models.IntegerField(default = 0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _("Leave Report Employee")
        verbose_name_plural = _("Leave Report Employees")

    def __str__(self):
        return f'{self.employee.user.first_name} {self.employee.user.last_name} {self.employee.user.other_name}'

    def get_absolute_url(self):
        return reverse("leavereportemployee-detail", kwargs={"pk": self.pk})
    
class FeedBackEmployee(models.Model):
    
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    feedback = models.TextField()
    feedback_reply = models.TextField(blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

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
    updated_at = models.DateTimeField( auto_now_add=True)
    objects = models.Manager()

    class Meta:
        verbose_name = _("Notification Employee")
        verbose_name_plural = _("Notification Employees")


    def __str__(self):
        return f'{self.employee_id.user.first_name} {self.employee_id.user.last_name} {self.employee_id.user.other_name}'
