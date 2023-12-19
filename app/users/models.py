from django.db import models
from django.contrib.auth.models import User
from datetime import date

class ToDoItem(models.Model):

    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    created_date = models.DateField(default=date.today)
    due_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=20)
    image = models.ImageField(upload_to='todo_images/', null=True, blank=True) 
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title