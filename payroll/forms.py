from django import forms
from django.forms import ModelForm

from .models import PayrollManager, PayrollManagerUpload


# for payroll manager form  /
class PayrollManagerForm(forms.ModelForm):
    class Meta:
        model = PayrollManager
        fields = '__all__'


# for payroll manager form  /
class PayrollManagerUploadForm(forms.ModelForm):
    class Meta:
        model = PayrollManagerUpload
        fields =('file_name',)