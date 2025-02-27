from django import forms
from .models import Task  

class TaskForm(forms.ModelForm):  
    class Meta:
        model = Task 
        fields = ['title', 'description', 'complete', 'due_date']  
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter task...'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Enter description...'}),
            'due_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}), 
        }