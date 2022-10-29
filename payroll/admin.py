from django.contrib import admin
from .models import *


admin.site.register(PayrollManager)
admin.site.register(PayrollManagerUpload)
admin.site.register(PayGroup)
admin.site.register(PayGrade)
admin.site.register(JobRole)
admin.site.register(EmployeeData)
admin.site.register(SalaryAttributeValues)
admin.site.register(DeductionAttributeValues)