from django import forms
from managements.models import * 

class DepartmentForm(forms.ModelForm):
    """
        DEPARTMENT FORM FOR EACH EMPLOYEE CREATED/UPDATED
    """
    class Meta:
        model = Department
        fields = ('name',)


class UploadEmployeeForm(forms.ModelForm):
    """
    HRM CREATING/UPDATING EMPLOYEE FORM
    """
    class  Meta:
        model = UploadEmployee
        fields = ("file_name",)