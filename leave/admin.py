from django.contrib import admin

# Register your models here.
from .models import (FeedBackAdmin, FeedBackEmployee, LeaveReportAdmin,
                     LeaveReportEmployee, NotificationAdmin,
                     NotificationEmployee)

admin.site.register(LeaveReportEmployee)
admin.site.register(FeedBackEmployee)
admin.site.register(NotificationEmployee)
admin.site.register(LeaveReportAdmin)
admin.site.register(FeedBackAdmin)
admin.site.register(NotificationAdmin)