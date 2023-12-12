from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse, reverse_lazy
from django.views import generic
from django import forms
from .models import Task, User, Comment
from django.core.exceptions import ValidationError
from django.contrib.auth.decorators import login_required
from .forms import UserUpdateForm, CommentPostingForm

class IndexView(LoginRequiredMixin, generic.ListView):
    login_url = "login"
    redirect_field_name = login_url
    template_name = "task_app/index.html"
    context_object_name = "task_list"
    
    def get_queryset(self) -> QuerySet[Any]:
        return Task.objects.order_by("due_date").filter(is_completed=False)

class IndexViewCompleted(LoginRequiredMixin, generic.ListView):
    login_url = "login"
    redirect_field_name = login_url
    template_name = "task_app/index_completed.html"
    context_object_name = "task_list"
    
    def get_queryset(self) -> QuerySet[Any]:
        return Task.objects.order_by("due_date").filter(is_completed=True)

def task_detail(request, pk):
    task = Task.objects.get(pk=pk)
    comments = task.comments.all()

    if request.method == 'POST':
        form = CommentPostingForm(request.POST)
        if form.is_valid():
            creating_comment = form.save(commit=False)
            creating_comment.created_by = request.user
            creating_comment.task = task
            creating_comment.save()
            return redirect('task_app:detail', pk=task.pk)
    else:
        form = CommentPostingForm()

    context = {
        'task': task,
        'comments': comments,
        'form': form
    }
    return render(request, 'task_app/detail.html', context)

def delete_comment(request, pk, comment_id=None):
    task = Task.objects.get(pk=pk)
    comment = get_object_or_404(Comment, pk=comment_id)
    comment.delete()
    return redirect('task_app:detail', pk = task.pk)

def complete_task(request, pk):
    task = Task.objects.get(pk=pk)
    task.is_completed = True
    task.save()
    return redirect('task_app:detail', pk = task.pk)

class TaskDetailView(generic.DetailView):
    model = Task
    template_name = "task_app/detail.html"
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentPostingForm()
        return context 
    
class UserDetailView(generic.DetailView):
    model = User
    template_name = "task_app/user_detail.html"
    
class UpdateView(LoginRequiredMixin, generic.UpdateView):
    login_url = "login"
    redirect_field_name = login_url
    model = Task
    fields = ["name", "description", "due_date", "is_completed"]
    template_name = "task_app/update.html"
    success_url = reverse_lazy("task_app:index")
    
    def get_form(self):
        form = super(UpdateView, self).get_form()
        form.fields['due_date'].widget = forms.TextInput(attrs={'type':'datetime-local'})
        form.fields['name'].widget.attrs['class'] = 'form-control'
        return form
    
    def form_valid(self, form):
        if form.instance.created_by != self.request.user:
            raise ValidationError("You cannot edit a task that is not yours")
        else:
            return super().form_valid(form)
            
# class UserUpdateView(LoginRequiredMixin, generic.UpdateView):
#     login_url = "login"
#     redirect_field_name = login_url
#     model = User
#     fields = ["username", "first_name", "last_name", "email"]
#     template_name = "task_app/user_update.html"
#     success_url = reverse_lazy("task_app:user_detail")
#     def get_form(self):
#         form = super(UserUpdateView, self).get_form()
#         form.fields['first_name'].widget.attrs['required'] = True
#         return form
        
def user_update(request, pk):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, initial={'username': request.user.username})
        if form.is_valid():
            user = form.save()
            return redirect('task_app:user_detail')
    else:
        form = UserUpdateForm()
    return render(request, 'task_app/user_update.html', {'form': form})


class TaskCreateView(LoginRequiredMixin, generic.CreateView):
    login_url = "login"
    redirect_field_name = login_url
    success_url = reverse_lazy("task_app:index")
    model = Task
    fields = ["name", "description", "due_date", "is_completed"]
    template_name = "task_app/create.html"
    
    def get_form(self):
        form = super(TaskCreateView, self).get_form()
        form.fields['description'].widget = forms.Textarea(attrs={"rows":"5", "class":"form-control"})
        for visible in form.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
        form.fields['due_date'].widget = forms.TextInput(attrs={'type':'datetime-local'})
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