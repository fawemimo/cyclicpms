from django import forms
from todo.models import Todo


class TodoForm(forms.ModelForm):
    # description = forms.CharField(max_length=255)

    class Meta:
        model = Todo
        fields = ('description','is_completed')
        widgets = {"description": forms.TextInput(attrs={"type": "text", "placeholder": "Add a New Task + Enter"})}
