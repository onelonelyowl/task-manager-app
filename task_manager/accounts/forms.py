from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True
    email = forms.EmailField(max_length=200, help_text='Required.')
    class Meta:
        model = User
        help_texts = {
            'first_name': 'Required.',
            'last_name': 'Required.'
        }
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']