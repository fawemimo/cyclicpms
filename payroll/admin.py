from django.contrib import admin

from .models import PayrollManager, PayrollManagerUpload
# from import_export.admin import ImportExportModelAdmin


admin.site.register(PayrollManager)
admin.site.register(PayrollManagerUpload)

