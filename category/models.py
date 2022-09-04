from django.db import models
from django.shortcuts import reverse
from django.utils.translation import gettext_lazy as _

from directors.models import Director
# Create your models here.
from managements.models import Employee

'''
SETTINGS UP CATEGORIES FOR EMPLOYEE:- This models show the set up for each employees in their respective

department, position, level, grade and step

Set up by the director of the  company
'''

class Department(models.Model):
       
    director        = models.ForeignKey(Director,on_delete=models.CASCADE,null=True,blank=True)
    name            = models.CharField(max_length=100)
    date_created    = models.DateTimeField(auto_now_add=True,blank=True,null=True)


    def __str__(self):

        return str(self.name)

    class Meta:
        verbose_name = ("Department")
        verbose_name_plural = ("Departments")


class Position(models.Model):
       
    director        = models.ForeignKey(Director,on_delete=models.CASCADE,null=True,blank=True)
    name            = models.CharField(max_length=100)
    department      = models.ForeignKey(Department, on_delete=models.CASCADE,null=True,blank=True)
    date_created = models.DateTimeField(auto_now_add=True,blank=True,null=True)

    def __str__(self):

        return f' {self.department} - {self.name}'

    class Meta:
        verbose_name = ("Position")
        verbose_name_plural = ("Positions")
          
class Level(models.Model):
    director        = models.ForeignKey(Director,on_delete=models.CASCADE,null=True,blank=True)
    name            = models.CharField(max_length=100)
    position        = models.ForeignKey(Position,on_delete=models.CASCADE,null=True,blank=True)
    date_created    = models.DateTimeField(auto_now_add=True,blank=True,null=True)

    def __str__(self):

        return f'{ self.position} - {self.name}'

    class Meta:
        verbose_name = ("Level")
        verbose_name_plural = ("Levels")

class Grade(models.Model):
    director        = models.ForeignKey(Director,on_delete=models.CASCADE,null=True,blank=True)
    name            = models.CharField(max_length=100)
    level           = models.ForeignKey(Level, on_delete=models.CASCADE,blank=True,null=True)
    date_created    = models.DateTimeField(auto_now_add=True,blank=True,null=True)

    def __str__(self):
        return f'{self.level} - {self.name}'


    class Meta:
        verbose_name = ("Grade")
        verbose_name_plural = ("Grades")

class Step(models.Model):
   
    director        = models.ForeignKey(Director,on_delete=models.CASCADE,null=True,blank=True)
    name            = models.CharField(max_length=100)
    grade           = models.ForeignKey(Grade,on_delete=models.CASCADE,blank=True,null=True)
    date_created    = models.DateTimeField(auto_now_add=True,blank=True,null=True)

    def __str__(self):
        return f'{self.grade} - {self.name}'

    class Meta:
        verbose_name = ("Step")
        verbose_name_plural = ("Steps")

class Leave(models.Model):
       
    director        = models.ForeignKey(Director,on_delete=models.CASCADE,null=True,blank=True)
    days            = models.PositiveIntegerField()
    step            = models.ForeignKey(Step,on_delete=models.CASCADE,blank=True,null=True)
    date_created    = models.DateTimeField(auto_now_add=True,blank=True,null=True)

    def __str__(self):
        return f'{self.step} - {self.days}'

    class Meta:
        verbose_name = ("Leave")
        verbose_name_plural = ("Leaves")        



'''
ENDSETTINGS UP CATEGORIES FOR EMPLOYEE
'''


'''
This shows the actual adding of categories to each employee
'''


class AddCategory(models.Model):
    director                    = models.ForeignKey(Director,on_delete=models.CASCADE,null=True,blank=True) 
    department                  = models.ForeignKey(Department,on_delete = models.SET_NULL,null=True)
    position                    = models.ForeignKey(Position,on_delete = models.SET_NULL,null=True)
    level                       = models.ForeignKey(Level,on_delete = models.SET_NULL,null=True)
    grade                       = models.ForeignKey(Grade,on_delete = models.SET_NULL,null=True)
    step                        = models.ForeignKey(Step,on_delete = models.SET_NULL,null=True)
    leave                       = models.ForeignKey(Leave,on_delete = models.SET_NULL,null=True)
    date_created                = models.DateTimeField(auto_now_add=True,blank=True,null=True)
    def __str__(self):
        return str(self.department)


    class Meta:
        verbose_name        = ("Category")
        verbose_name_plural = ("Categories")


# testing dependable dropdown 
class Car(models.Model):#level
    name = models.CharField(max_length=80)
    country = models.CharField(max_length=100)

    def __str__(self):
        return str(self.name)
    
class Model(models.Model):#grade
    name = models.CharField(max_length=50)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.car}-{self.name}"
# class Step     
class Order(models.Model):#employee categgory
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    model = models.ForeignKey(Model, on_delete=models.CASCADE)

def __str__(self):
    return str(self.pk)


