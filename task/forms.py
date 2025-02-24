from django import forms
from .models import Task  # Corregido: "task" → "Task"

class TaskForm(forms.ModelForm):  # Corregido: "taskForm" → "TaskForm"
    class Meta:
        model = Task  # Corregido: "task" → "Task"
        fields = ['title', 'description', 'complete']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter task...'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Enter description...'}),
        }
