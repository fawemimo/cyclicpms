import uuid

from django.db import models
from django.shortcuts import reverse
from django.utils.translation import gettext_lazy as _

from accounts.models import User

# Create your models here.








'''
DIRECTOR MODELS

'''

class Company(models.Model):
    name                            = models.CharField(max_length=225,blank=True,null=True,unique=True)
    company_tracking_id             = models.CharField(max_length=24,blank=True)    
    date_created                    = models.DateTimeField(auto_now_add=True,null=True)
    date_updated                    = models.DateTimeField(auto_now=True,null=True,blank=True)
    

    class Meta:
        verbose_name = "Company"
        verbose_name_plural = "Companies"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("company-detail", kwargs={"pk": self.pk})

    
    def save(self,*args, **kwargs):
        if self.company_tracking_id == "":
            date = self.date_created
            self.company_tracking_id = str(uuid.uuid4()).replace("-","").upper()[:24]
        return super().save(*args, **kwargs) 


class Director(models.Model):   
    user                        = models.OneToOneField(User,on_delete=models.CASCADE)
    company                     = models.ForeignKey(Company,on_delete=models.CASCADE,blank=True,null=True)    
    phone_number_2              = models.CharField(max_length=100,blank=True,null=True)
    contact_address             = models.CharField(max_length=255,blank=True,null=True)
    fcm_token                   = models.TextField(default='',blank=True,null=True)
    created_at                  = models.DateTimeField(auto_now_add=True)
    updated_at                  = models.DateTimeField(auto_now=True,blank=True,null=True)
    
    gender_type_choices         = (
        ('Male','Male'),
        ('Female','Female')
    )
    gender                      = models.CharField(max_length=50,choices=gender_type_choices,blank=True,null=True)
    verify_director             = models.BooleanField(default=False)
    profile_pic                 = models.FileField(default='avatar.png',upload_to = "media/",blank=True,null=True)
    class Meta:
        verbose_name = _("Director")
        verbose_name_plural = _("Directors")

    def __str__(self):
        return f'{ self.user.first_name } { self.user.last_name } { self.user.other_name }'

    def get_absolute_url(self):
        return reverse("director-detail", kwargs={"pk": self.pk})
    






'''
END DIRECTOR MODELS
'''