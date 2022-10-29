from decimal import Decimal

from category.models import AddCategory
from directors.models import Director
from django.core.validators import MinValueValidator
from django.db import models
from django.shortcuts import reverse
from django.utils.translation import gettext_lazy as _

# from payroll.models import EmployeeData


class SetSalary(models.Model):
    addcategory = models.ForeignKey(AddCategory, on_delete=models.PROTECT)
    hours_worked = models.PositiveIntegerField()
    hourly_pay_rate = models.PositiveIntegerField()
    overtime_hours = models.PositiveIntegerField(blank=True, null=True)
    overtime_multiplier = models.FloatField(blank=True, null=True)
    annual_gross_pay = models.PositiveIntegerField(blank=True, null=True)

    def get_annual_gross_pay(self):
        regular_pay = self.hours_worked * self.hourly_pay_rate
        print(regular_pay)
        if self.overtime_hours > 0 and self.overtime_multiplier > 0:
            overtime_regular_pay = (self.hours_worked * self.hourly_pay_rate) + (
                (self.overtime_hours * self.hourly_pay_rate) * (self.overtime_multiplier)
            )
            print(overtime_regular_pay)
            return overtime_regular_pay

        else:
            regular_pay = self.hours_worked * self.hourly_pay_rate
            print(regular_pay)
            return regular_pay

    def save(self, *args, **kwargs):
        self.annual_gross_pay = self.get_annual_gross_pay()
        super(SetSalary, self).save(*args, **kwargs)

    class Meta:
        verbose_name = _("Set Salary")
        verbose_name_plural = _("Set Salaries")

    def __str__(self):
        return str(self.addcategory)

    def get_absolute_url(self):
        return reverse("set-salary_detail", kwargs={"pk": self.pk})


class PaymentAttribute(models.Model):
    """
    Setting Up a Payment Attribute for various company
    """

    director = models.ForeignKey(Director, on_delete=models.DO_NOTHING, blank=True, null=True)
    name = models.CharField(max_length=255,help_text = "format: Payment attribute could be that one of Earnings or Deductions")
    definations = models.CharField(max_length=255) 
                         
    def __str__(self):
        return f'{self.director}- {self.name} '

    class Meta:
        verbose_name = "Payment Attribute"
        verbose_name_plural = "Payment Attributes"
        unique_together = (("director","name"),)


class SalaryAttributeValue(models.Model):
    """
    Relating to salary attribute for the specifics value
    """

    director = models.ForeignKey(Director, on_delete=models.DO_NOTHING, blank=True, null=True)
    salary_attribute_value = models.ForeignKey(
        PaymentAttribute, on_delete=models.CASCADE, related_name="salaryattributevaluess"
    )
    value = models.DecimalField(max_digits=50, decimal_places=2, validators=[MinValueValidator(Decimal("0.00"))])

    def __str__(self):
        return f"{self.director}:{self.salary_attribute_value.name} - {self.value}"

    class Meta:
        verbose_name = "Salary Attribute Value"
        verbose_name_plural = "Salary Attribute Values"


# class DeductionAttribute(models.Model):
#     """
#     Employee Deductions Attribute
#     """

#     director = models.ForeignKey(Director, on_delete=models.DO_NOTHING, blank=True, null=True)
#     name = models.CharField(max_length=255, unique=True)
#     definations = models.CharField(max_length=255)

#     def __str__(self):
#         return self.name

#     class Meta:
#         verbose_name = "Deduction Attribute"
#         verbose_name_plural = "Deduction Attributes"


class DeductionAttributeValue(models.Model):

    """
    Deduction Attribute relating to Deduction Attribute value
    """

    director = models.ForeignKey(Director, on_delete=models.DO_NOTHING, blank=True, null=True)
    deduction_attribute = models.ForeignKey(PaymentAttribute, on_delete=models.PROTECT)
    attribute_value = models.DecimalField(
        max_digits=50, decimal_places=2, validators=[MinValueValidator(Decimal("0.00"))]
    )

    def __str__(self):
        return f"{self.deduction_attribute.name} - {self.attribute_value}"

    class Meta:
        verbose_name = "Deduction Attribute Value"
        verbose_name_plural = "Deduction Attribute Values"
