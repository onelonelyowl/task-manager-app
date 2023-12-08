from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.messages.views import SuccessMessageMixin
from django import forms
from django.contrib.auth import get_user_model
from .forms import UserRegisterForm
from django.shortcuts import render, redirect
from django.contrib.auth import login
User = get_user_model()

def signup(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('tasks')
    else:
        form = UserRegisterForm()
    return render(request, 'registration/signup.html', {'form': form})

class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    username = UsernameField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Username', 'id': 'username'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Password',
            'id': 'password',
        }
))


# class RegisterView(SuccessMessageMixin, generic.CreateView):
#     form_class = UserCreationForm
#     success_url = reverse_lazy("login")
#     template_name = "registration/signup.html"
#     success_message = "Your profile was created successfully"
    # put custom classes for form here and also require first and last name and email etc