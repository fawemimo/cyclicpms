from django.contrib import admin
from managements.hrm.tasks import leave_management
# Register your models here.
from .models import (FeedBackAdmin, FeedBackEmployee, LeaveReportAdmin,
                     LeaveReportEmployee, NotificationAdmin,
                     NotificationEmployee)


class LeaveReportEmployeeAdmin(admin.ModelAdmin):
    list_display = ('employee','leave_start','leave_end','total_duration_days','is_on_leave')

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        leave_management.delay()

admin.site.register(LeaveReportEmployee,LeaveReportEmployeeAdmin)


admin.site.register(FeedBackEmployee)
admin.site.register(NotificationEmployee)
admin.site.register(LeaveReportAdmin)
admin.site.register(FeedBackAdmin)
admin.site.register(NotificationAdmin)