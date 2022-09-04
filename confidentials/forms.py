from django import forms
from django.db.models import fields
from django.forms import widgets

from .models import *


class BankDetailForm(forms.ModelForm):
    class Meta:
        model = BankDetail
        fields = '__all__'
        widgets = {
            'bank_name':forms.TextInput(attrs={
                'type':'text',
                'class':'form-control'
                
                
            }),
            'full_name':forms.TextInput(attrs={
                'type':'text',
                'class':'form-control'
                
                
            }),'bvn':forms.TextInput(attrs={
                'type':'text',
                'class':'form-control'
                
                
            }),'account_number':forms.TextInput(attrs={
                'type':'text',
                'class':'form-control'
                
                
            }),'sort_code':forms.TextInput(attrs={
                'type':'text',
                'class':'form-control'
                
                
            })
        }
class PersonalInfoForm(forms.ModelForm):
    class Meta:
        model = PersonalInfo
        fields = '__all__'        
        
class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = '__all__'
        
    def __init__(self,*args, **kwargs):
        super(EducationForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
                
                
class FileUploadForm(forms.ModelForm):
    model = FileUpload
    fields = ('file',)