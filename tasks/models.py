from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Task Category Model
class TaskCategory(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

# Task Model
class Task(models.Model):

    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('in-progress', 'In Progress'),
        ('completed', 'Completed'),
    )
    name = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    created_at = models.DateTimeField(default=timezone.now)
    

    

    def __str__(self):
        return self.name 