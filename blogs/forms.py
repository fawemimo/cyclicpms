from django import forms
from django.forms import ModelForm

from .models import Post

# from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
# from django_summernote.fields import SummernoteTextFormField, SummernoteTextField

class PostForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = ['title','content']
        # exclude = ('author',)
        widgets = {
            'author':forms.TextInput(attrs={
                'type':'hidden',
            }),
            
        }    
