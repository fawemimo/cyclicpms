from django import forms
from .models import Subscriber, MailMessage,ContactRequest
from django.forms import ModelForm
# from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
# from django_summernote.fields import SummernoteTextFormField, SummernoteTextField

class ContactRequestForm(forms.ModelForm):
    # descriptions = SummernoteTextField()
    class Meta:
        model = ContactRequest
        fields = '__all__'
        exclude = ('date_contacted','date_review')
        widgets = {
            # 'descriptions':SummernoteWidget(),
            'email':forms.TextInput(attrs={
                'type':'text',
                'class':'form-control',
                'placeholder':'Enter email',
                'id':'exampleInputEmail'}),
            'full_name':forms.TextInput(attrs={
                'placeholder':'Enter full name',
                'type':'text',
                'class':'form-control',
                'id':'exampleInputEmail'}),
            'phone':forms.TextInput(attrs={
                'placeholder':'+(xxx)',
                'type':'text',
                'class':'form-control',
                'id':'exampleInputEmail'}),
        }
        
        
#  subscribers form  

class SubscribersForm(forms.ModelForm):
    email = forms.EmailField(label='Email address')
    class Meta:
        model = Subscriber
        fields = ('email',)       


# for sending messages 

class MailMessagesForm(forms.ModelForm):
    title = forms.CharField(max_length=255)
    # message = SummernoteTextField()

    class Meta:
        model = MailMessage
        fields = ['title','message']
        exclude = ('date_messaged',)
        widgets = {
            # 'message': SummernoteWidget(),
            # 'title': SummernoteInplaceWidget()
        }