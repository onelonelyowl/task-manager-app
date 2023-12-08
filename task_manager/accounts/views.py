from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django.urls import reverse_lazy
from django.views import generic
from django import forms
from django.contrib.auth import get_user_model
User = get_user_model()


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


class RegisterView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"
    # put custom classes for form here and also require first and last name and email etc