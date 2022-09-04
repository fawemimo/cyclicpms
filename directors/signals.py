# from accounts.models import  User
# from django.db.models.signals import post_save
# from django.dispatch import receiver

# from directors.models import Director, Company
# import uuid

# @receiver(post_save, sender=User)        
# def create_user_profile(sender,instance,created,*args,**kwargs):
#     print('sender', sender)
#     print('created', created)
#     print('instance', instance)
#     if created:   
#         if instance.user_type==5:     
#             Director.objects.create(user=instance)
            
            
            
            
#             print('created', created)
#             print('instance', instance)
            
# @receiver(post_save, sender=User)
# def save_profile(sender, instance,*args, **kwargs):
#     if instance.user_type==5: 
#         instance.director.save()      
    
#         print('instance', instance)      
    
# @receiver(post_save, sender=Director)        
# def create_user_director(sender,instance,created,*args,**kwargs):
#     print('sender', sender)
#     print('created', created)
#     print('instance', instance)
#     if created:        
#             Company.objects.create(director=instance,name='')
#             # Company.objects.create(DIRECTOR=instance)
            
            
#             print('created', created)
#             print('instance', instance)
            
# # @receiver(post_save, sender=Director)
# # def save_director(sender, instance, **kwargs):
# #     instance.company.save()      
         