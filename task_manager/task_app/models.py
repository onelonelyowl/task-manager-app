from django.db import models

class Task(models.Model):
    name = models.CharField("Task name", max_length=200)
    description = models.CharField("Task description", max_length=500)
    due_date = models.DateTimeField("Due date")
    is_completed = models.BooleanField("Is completed")