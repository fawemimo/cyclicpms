from django import forms
from .models import LeaveReportEmployee

class LeaveReportEmployeeForm(forms.ModelForm):
    class Meta:
        model = LeaveReportEmployee
        fields = (
            'leave_reason',
            'leave_start',
            'leave_end',
        )