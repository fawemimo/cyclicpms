from django.contrib import admin

from managements.models import Employee, EmployeeRole, Department,UploadEmployee

# Employee Admin models
admin.site.register(Employee)
admin.site.register(EmployeeRole)
admin.site.register(Department)
admin.site.register(UploadEmployee)