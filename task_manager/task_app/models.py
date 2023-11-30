from django.db import models
from django.utils import timezone
from django.conf import settings

class Task(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField("Task name", max_length=200, default="placeholder")
    description = models.CharField("Task description", max_length=500)
    due_date = models.DateTimeField("Due date")
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    is_completed = models.BooleanField("Is completed")
    def is_overdue(self):
        return self.due_date <= timezone.now()