from django import forms
from django.forms import fields 

from .models import *

class AddCategoryForEmployeeForm(forms.ModelForm):
    class Meta:
        model = AddCategoryForEmployee
        fields = '__all__'
        widget = {
            'employee':forms.TextInput(attrs={
                'type':'select',
                'placeholder':'employee name',
                'class':'form-control',
                'name':'employee'
            }),
           'level':forms.TextInput(attrs={
                'type':'select',
                'placeholder':'level ',
                'class':'form-control',
                'name':'level'
            }),
           'grade':forms.TextInput(attrs={
                'type':'select',
                'placeholder':'grade ',
                'class':'form-control',
                'name':'grade'
            }),
           'steps':forms.TextInput(attrs={
                'type':'select',
                'placeholder':'steps ',
                'class':'form-control',
                'name':'steps'
            }),
           'annual_gross_pay':forms.TextInput(attrs={
                'type':'text',
                'placeholder':'annual_gross_pay ',
                'class':'form-control',
                'name':'annual_gross_pay'
            }),
            'annual_net_pay':forms.TextInput(attrs={
                'type':'text',
                'placeholder':'annual_net_pay ',
                'class':'form-control',
                'name':'annual_net_pay'
            }),
            'leave_allocation_days':forms.TextInput(attrs={
                'type':'text',
                'placeholder':'leave_allocation_days ',
                'class':'form-control',
                'name':'leave_allocation_days'
            }),
               
        }
        
    def __init__(self,*args,**kwargs):
        super().__init__(*args, **kwargs)
        self.fields['grade'].queryset = Grade.objects.none()
        
        if 'level' in self.data:
            try:
                level_id = int(self.data.get('level'))
                self.fields['grade'].queryset = Grade.objects.filter(level_id=level_id)
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['grade'].queryset = self.instance.level.grade_set