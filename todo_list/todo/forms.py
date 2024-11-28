from django import forms
from .models import Todo

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'details']  # Include fields from the model
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter task title',
                'required': True,
            }),
            'details': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter task details',
                'rows': 3,
                'required': True,
            }),
        }