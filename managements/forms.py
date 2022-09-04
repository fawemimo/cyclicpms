from django import forms
from django.contrib.auth.forms import UserCreationForm
from accounts.models import User
from .models import Employee, Admin

class UserSearchForm(forms.ModelForm):
    
    class Meta:
        model           = User
        fields          = ("first_name","last_name","other_name")

class UserExtendedForm(UserCreationForm):
    email               = forms.EmailField(required=True)
    first_name          = forms.CharField(max_length=100, required=True)
    last_name           = forms.CharField(max_length=100, required=True)    
    user_type           = forms.CharField(initial='is_employee',widget=forms.TextInput(attrs={'type':'hidden'}))
    class Meta:
        model           = User
        fields          = ("username","email","first_name","last_name","other_name","password1","password2","phone_number")

    def save(self,commit=True):
        user = super().save(commit=False)
        
        user.email          = self.cleaned_data['email']
        user.first_name     = self.cleaned_data['first_name']
        user.last_name      = self.cleaned_data['last_name']
        
        if commit:
            user.save()
        return user    
    
# FOR SEARCH QUERY  
    
class EmployeeForm(forms.ModelForm):
    
    class Meta:
        model = Employee
        fields = ("employee_unique_id",)
        widgets = {
        'department':forms.TextInput(attrs={
            'type':'text',
            'class':'form-control',
            'placeholder':'Enter department',
            'id':'exampleInputEmail',
            'name':'department'}),
        'employee_unique_id':forms.TextInput(attrs={
            'type':'text',
            'class':'form-control',
            'placeholder':'Enter employee ID',
            'id':'exampleInputEmail',
            'name':'employee_unique_id'}),
        
        }
        
        
class AdminForm(forms.ModelForm):
    
    class Meta:
        model = Admin
        fields = ("department","admin_unique_id")
        widgets = {
        
        'department':forms.TextInput(attrs={
            'type':'text',
            'class':'form-control',
            'placeholder':'Enter department',
            'id':'exampleInputEmail'}),
        'admin_unique_id':forms.TextInput(attrs={
            'type':'text',
            'class':'form-control',
            'placeholder':'Enter admin ID',
            'id':'exampleInputEmail'}),
        }