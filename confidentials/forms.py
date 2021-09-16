from django import forms
from .models import *


class BankDetailForm(forms.ModelForm):
    class Meta:
        model = BankDetail
        fields = '__all__'
        
class PersonalInfoForm(forms.ModelForm):
    class Meta:
        model = PersonalInfo
        fields = '__all__'        