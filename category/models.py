from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.shortcuts import reverse
# Create your models here.
from managements.models import Employee
class Level(models.Model):
    """
    Description: Model Description
    """

    level       = models.CharField(max_length=100)


    def __str__(self):

        return str(self.level)

    class Meta:
        verbose_name = ("Level")
        verbose_name_plural = ("Levels")

class Grade(models.Model):
    """
    Description: Model Description
    """
    level       = models.ForeignKey(Level, on_delete=models.CASCADE)
    grade       = models.CharField(max_length=100)


    def __str__(self):
        return f'{self.level} - {self.grade}'


    class Meta:
        verbose_name = ("Grade")
        verbose_name_plural = ("Grades")

class Step(models.Model):
    """
    Description: Model Description
    """

    step       = models.CharField(max_length=100)


    def __str__(self):
        return str(self.step)

    class Meta:
        verbose_name = ("Step")
        verbose_name_plural = ("Steps")


class AddCategoryForEmployee(models.Model):
    """
    Description: Model DescriptionGo to your <b>special offers</b> page to see now.
    """
    employee                    = models.ForeignKey(Employee,on_delete = models.CASCADE)
    level                       = models.ForeignKey(Level,on_delete = models.SET_NULL,null=True)
    grade                       = models.ForeignKey(Grade,on_delete = models.SET_NULL,null=True)
    steps                       = models.ForeignKey(Step,on_delete = models.SET_NULL,null=True)
    annual_gross_pay            = models.PositiveSmallIntegerField()
    annual_net_pay              = models.PositiveSmallIntegerField()
    leave_allocation_days       = models.PositiveSmallIntegerField()
    

    def __str__(self):
        return str(self.pk)


    class Meta:
        verbose_name        = ("Category")
        verbose_name_plural = ("Categories")
