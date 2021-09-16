from django.contrib import admin

# Register your models here.
from .models import LeaveReportEmployee, FeedBackEmployee,NotificationEmployee

admin.site.register(LeaveReportEmployee)
admin.site.register(FeedBackEmployee)
admin.site.register(NotificationEmployee)
