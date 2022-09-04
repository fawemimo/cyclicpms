from django.contrib import admin

# Register your models here.
from set_salary.models import SetSalary


class SetSalaryAdmin(admin.ModelAdmin):
    list_display = ('addcategory','annual_gross_pay')
admin.site.register(SetSalary,SetSalaryAdmin)