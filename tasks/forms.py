from django import forms
from .models import Task, TaskCategory

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'description', 'status']
