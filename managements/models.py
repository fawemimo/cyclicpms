# Create your models here.
import uuid

from django.db import models
from django.shortcuts import reverse
from django.utils.translation import gettext_lazy as _

from accounts.models import User
from directors.models import Director


# Uploads file for bulk creations of employee 
class UploadEmployee(models.Model):
    
    file_name                   = models.FileField(upload_to='employeecreation')
    uploaded                    = models.DateField(auto_now_add=True)
    activated                   = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = ("Bulk Creation")
        verbose_name_plural = ("Bulk Creations")    



class Employee(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    director = models.ForeignKey(
    Director, on_delete=models.CASCADE, blank=True, null=True)
    employee_unique_id = models.CharField(max_length=6, blank=True)
    dob = models.DateField(blank=True, null=True)
    phone_number_2 = models.CharField(max_length=100, blank=True, null=True)
    contact_address = models.CharField(max_length=255, blank=True, null=True)
    fcm_token = models.TextField(default='', blank=True, null=True)
    date_employed = models.DateTimeField(_("Date Employed"), auto_now_add=True)
    gender_type_choices = (
        ('Male', 'Male'),
        ('Female', 'Female')
    )
    gender = models.CharField(
        max_length=50, choices=gender_type_choices, blank=True, null=True)
    profile_pic = models.FileField(
        default='avatar.png', upload_to="media/", blank=True, null=True)
    date_updated = models.DateTimeField(_("Date Updated"), auto_now=True,blank=True,null=True)
    class Meta:
        verbose_name = ("Employee")
        verbose_name_plural = ("Employees")

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name} {self.user.other_name} '

    def save(self, *args, **kwargs):
        if self.employee_unique_id == "":
            self.employee_unique_id = str(
                uuid.uuid4()).replace("-", "").upper()[:6]
        return super().save(*args, **kwargs)

# creating user privileges
class EmployeePrivilege(models.Model):
    Employee_role = models.OneToOneField(
        Employee,on_delete=models.DO_NOTHING
    )
    can_edit_update = models.BooleanField(
        default=False
    )
    can_delete = models.BooleanField(
        default=False
    )
    
    def __str__(self):
        pass

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'EmployeePrivilege'

        verbose_name_plural = 'EmployeePrivileges'



class Admin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    admin_unique_id = models.CharField(max_length=6, blank=True)
    dob = models.DateField(blank=True, null=True)
    phone_number_2 = models.CharField(max_length=100, blank=True, null=True)
    contact_address = models.CharField(max_length=255, blank=True, null=True)
    # changing this to foreign key
    department = models.CharField(
        _("Dapartment/Units"), max_length=255, blank=True, null=True)
    fcm_token = models.TextField(default='', blank=True, null=True)
    date_employed = models.DateTimeField(_("Date Employed"), auto_now_add=True)
    gender_type_choices = (
        ('Male', 'Male'),
        ('Female', 'Female')
    )
    gender = models.CharField(max_length=50, choices=gender_type_choices)

    profile_pic = models.FileField(
        default='avatar.png', upload_to="media/", blank=True, null=True)

    class Meta:
        verbose_name = ("Admin")
        verbose_name_plural = ("Admins")

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name} {self.user.other_name} '

    def save(self, *args, **kwargs):
        if self.admin_unique_id == "":
            self.admin_unique_id = str(
                uuid.uuid4()).replace("-", "ADM").upper()[:6]
        return super().save(*args, **kwargs)


'''
Profile pics for employee
'''
# class PicsEmployee(models.Model):

#     employee            = models.ForeignKey(Employee,on_delete=models.CASCADE)
#     profile_pic         = models.ImageField(upload_to="profile_pics/%Y/%m/%d",default='avatar.png')

#     class Meta:
#         verbose_name = _("PicsEmployee")
#         verbose_name_plural = _("Pics Employees")

#     def __str__(self):
#         return f'{ self.employee.user.first_name } { self.employee.user.last_name } { self.employee.user.other_name }'

#     def get_absolute_url(self):
#         return reverse("PicsEmployee_detail", kwargs={"pk": self.pk})


# '''
# Profile pics for Admin
# '''

# class PicsAdmin(models.Model):

#     admin                = models.ForeignKey(Admin,on_delete=models.CASCADE)


#     class Meta:
#         verbose_name = _("PicsAdmin")
#         verbose_name_plural = _("Pics Admins")

#     def __str__(self):
#         return f'{ self.admin.user.first_name } { self.admin.user.last_name } { self.admin.user.other_name }'

#     def get_absolute_url(self):
#         return reverse("PicsAdmin_detail", kwargs={"pk": self.pk})
