from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.shortcuts import reverse
from accounts.models import User



# Create your models here.
import uuid


class Company(models.Model):

    company_name            = models.CharField(max_length=225,blank=True,null=True)

    class Meta:
        verbose_name = _("Company")
        verbose_name_plural = _("Companies")

    def __str__(self):
        return self.company_name

    def get_absolute_url(self):
        return reverse("company-detail", kwargs={"pk": self.pk})


class Employee(models.Model):

    user                        = models.OneToOneField(User,on_delete=models.CASCADE)
    employee_unique_id          = models.CharField(max_length=6,blank=True)
    dob                         = models.DateField(blank=True,null=True)
    phone_number_2              = models.CharField(max_length=100,blank=True,null=True)
    contact_address             = models.CharField(max_length=255,blank=True,null=True)
    # company                     = models.ForeignKey(Company,on_delete = models.DO_NOTHING,max_length=255,blank=True,null=True)
    company_name                = models.CharField(max_length=100,blank=True,null=True)
    department                  = models.CharField(_("Dapartment/Units"),max_length=255,blank=True,null=True)
    fcm_token                   = models.TextField(default='')
    date_employed               = models.DateTimeField(_("Date Employed"),auto_now_add=True)
    gender_type_choices         = (
        ('Male','Male'),
        ('Female','Female')
    )
    gender                      = models.CharField(max_length=50,choices=gender_type_choices,blank=True,null=True)
       

    class Meta:
        verbose_name = ("Employee")
        verbose_name_plural = ("Employees")

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name} {self.user.other_name} '
    
    def save(self,*args, **kwargs):
        if self.employee_unique_id == "":
            self.employee_unique_id = str(uuid.uuid4()).replace("-","").upper()[:6]
        return super().save(*args, **kwargs) 

    
class Admin(models.Model):
    
    user                        = models.OneToOneField(User,on_delete=models.CASCADE)
    admin_unique_id             = models.CharField(max_length=6,blank=True)
    dob                         = models.DateField(blank=True,null=True)
    phone_number_2              = models.CharField(max_length=100,blank=True,null=True)
    # company                     = models.ForeignKey(Company,on_delete = models.CASCADE,max_length=255,blank=True,null=True)
    company_name                = models.CharField(max_length=100,blank=True,null=True)
    contact_address             = models.CharField(max_length=255,blank=True,null=True)
    department                  = models.CharField(_("Dapartment/Units"),max_length=255,blank=True,null=True)
    fcm_token                   = models.TextField(default='',blank=True,null=True)
    date_employed               = models.DateTimeField(_("Date Employed"),auto_now_add=True)
    gender_type_choices         = (
        ('Male','Male'),
        ('Female','Female')
    )
    gender                      = models.CharField(max_length=50,choices=gender_type_choices)


    class Meta:
        verbose_name = ("Admin")
        verbose_name_plural = ("Admins")

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name} {self.user.other_name} '

    def save(self,*args, **kwargs):
        if self.admin_unique_id == "":
            self.admin_unique_id = str(uuid.uuid4()).replace("-","ADM").upper()[:6]
        return super().save(*args, **kwargs)


    
