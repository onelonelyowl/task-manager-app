from django.db import models
from django.utils import timezone

class Task(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField("Task name", max_length=200)
    description = models.CharField("Task description", max_length=500)
    due_date = models.DateTimeField("Due date")
    is_completed = models.BooleanField("Is completed")
    def is_overdue(self):
        return self.due_date <= timezone.now()