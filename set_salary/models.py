from django.db import models
from django.shortcuts import reverse
from django.utils.translation import ugettext_lazy as _

# Create your models here.
from category.models import AddCategory


class SetSalary(models.Model):   
    addcategory                 = models.ForeignKey(AddCategory,on_delete=models.CASCADE)
    hours_worked                = models.PositiveIntegerField()
    hourly_pay_rate             = models.PositiveIntegerField()
    overtime_hours              = models.PositiveIntegerField(blank=True,null=True)
    overtime_multiplier         = models.FloatField(blank=True,null=True)
    annual_gross_pay            = models.PositiveIntegerField(blank=True,null=True)
    
    
    
    def get_annual_gross_pay(self):
        regular_pay = self.hours_worked * self.hourly_pay_rate
        print(regular_pay)        
        if self.overtime_hours > 0 and self.overtime_multiplier > 0 :
            overtime_regular_pay =((self.hours_worked * self.hourly_pay_rate) + ((self.overtime_hours * self.hourly_pay_rate) * (self.overtime_multiplier)))
            print(overtime_regular_pay)
            return overtime_regular_pay
        
        else:
            regular_pay = self.hours_worked * self.hourly_pay_rate
            print(regular_pay)  
            return regular_pay
        
    def save(self,*args, **kwargs):
        self.annual_gross_pay = self.get_annual_gross_pay()
        super(SetSalary, self).save(*args, **kwargs)

    class Meta:
        verbose_name = _("Set Salary")
        verbose_name_plural = _("Set Salaries")

    def __str__(self):
        return str(self.addcategory)

    def get_absolute_url(self):
        return reverse("set-salary_detail", kwargs={"pk": self.pk})       