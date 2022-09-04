from django.contrib.auth import get_user_model
from .models import OtpCode, User
from django.db.models.signals import post_save
from django.dispatch import receiver
from managements.models import Employee, Admin

User = get_user_model()
@receiver(post_save, sender=User)
def post_save_generate_code(sender,instance,created,*args,**kwargs):
    if created:
        OtpCode.objects.create(user=instance)
        
@receiver(post_save, sender=User)        
def create_user_profile(sender,instance,created,*args,**kwargs):
    if created:
        if instance.user_type == 1:
            Employee.objects.create(user=instance)
            
        elif instance.user_type == 2:
            Admin.objects.create(user=instance)
            
            
        else:
            pass    
            
@receiver(post_save, sender=User)        
def save_user_profile(sender,instance,created,*args,**kwargs):
    if instance.user_type == 1:
        instance.employee.save()
        
    elif instance.user_type == 2:
        instance.admin.save()    
        
    else:
        pass