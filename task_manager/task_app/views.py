from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse, reverse_lazy
from django.views import generic

from .models import Task

class IndexView(generic.ListView):
    template_name = "task_app/index.html"
    context_object_name = "task_list"
    
    def get_queryset(self) -> QuerySet[Any]:
        return Task.objects.order_by("due_date")
    
class DetailView(generic.DetailView):
    model = Task
    template_name = "task_app/detail.html"
    
class UpdateView(generic.UpdateView):
    model = Task
    fields = ["name", "description", "due_date", "is_completed"]
    template_name = "task_app/update.html"
    
class CreateView(generic.CreateView):
    success_url = reverse_lazy("task_app:index")
    model = Task
    fields = ["name", "description", "due_date", "is_completed"]
    template_name = "task_app/create.html"
    
class DeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("task_app:index")
    template_name = "task_app/delete.html"