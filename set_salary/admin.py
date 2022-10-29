from django.contrib import admin

# Register your models here.
from set_salary.models import *


class SetSalaryAdmin(admin.ModelAdmin):
    list_display = ('addcategory','annual_gross_pay')
admin.site.register(SetSalary,SetSalaryAdmin)

admin.site.register(PaymentAttribute)
admin.site.register(SalaryAttributeValue)
# admin.site.register(DeductionAttribute)
admin.site.register(DeductionAttributeValue)