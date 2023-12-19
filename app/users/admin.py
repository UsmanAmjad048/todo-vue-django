# users/admin.py

from django.contrib import admin
from users.models import ToDoItem

admin.site.register(ToDoItem)