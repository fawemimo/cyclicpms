from django.db.models.signals import post_save
from django.dispatch import receiver
from managements.models import Employee, EmployeeRole
from payroll.models import EmployeeData


@receiver(post_save, sender=Employee)
def create_employee_role(sender,created,instance,*args, **kwargs):
    if created:
        EmployeeRole.objects.create(employee=instance)
        EmployeeData.objects.create(employee=instance)
        instance.save()
