from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import get_object_or_404, render
from django.urls import reverse, reverse_lazy
from django.views import generic
from django import forms
from .models import Task
from django.core.exceptions import ValidationError
from django.contrib.auth.decorators import login_required




class IndexView(LoginRequiredMixin, generic.ListView):
    login_url = "login"
    redirect_field_name = login_url
    template_name = "task_app/index.html"
    context_object_name = "task_list"
    
    def get_queryset(self) -> QuerySet[Any]:
        return Task.objects.order_by("due_date")


class DetailView(generic.DetailView):
    model = Task
    template_name = "task_app/detail.html"
    
class UpdateView(LoginRequiredMixin, generic.UpdateView):
    login_url = "login"
    redirect_field_name = login_url
    model = Task
    fields = ["name", "description", "due_date", "is_completed"]
    template_name = "task_app/update.html"
    success_url = reverse_lazy("task_app:index")

    
    def get_form(self):
        form = super(UpdateView, self).get_form()
        form.fields['due_date'].widget = forms.SelectDateWidget()
        form.fields['name'].widget.attrs['class'] = 'form-control'
        return form
    
    def form_valid(self, form):
        if form.instance.created_by != self.request.user:
            raise ValidationError("You cannot edit a task that is not yours")
        else:
            return super().form_valid(form)
            
    
    
class TaskCreateView(LoginRequiredMixin, generic.CreateView):
    login_url = "login"
    redirect_field_name = login_url
    success_url = reverse_lazy("task_app:index")
    model = Task
    fields = ["name", "description", "due_date", "is_completed"]
    template_name = "task_app/create.html"

    
    def get_form(self):
        form = super(TaskCreateView, self).get_form()
        for visible in form.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
        form.fields['due_date'].widget = forms.SelectDateWidget()
        form.fields['is_completed'].widget.attrs['class'] = 'form-check-input'

        return form
    
    def form_valid(self, form):
        form.instance.created_by = self.request.user
        ##### WE NEED TO HANDLE IF A USER IS NOT LOGGED IN HERE
        return super().form_valid(form)
    
class DeleteView(LoginRequiredMixin, generic.DeleteView):
    login_url = "login"
    redirect_field_name = login_url
    model = Task
    success_url = reverse_lazy("task_app:index")
    template_name = "task_app/delete.html"