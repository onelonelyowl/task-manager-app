from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Comment

class UserUpdateForm(forms.ModelForm):
    first_name = forms.CharField(max_length=200, required=True)
    last_name = forms.CharField(max_length=200, required=True)
    email = forms.EmailField(max_length=200, help_text='Required.')
    class Meta:
        model = User
        help_texts = {
            'first_name': 'Required.',
            'last_name': 'Required.'
        }
        fields = ['username', 'first_name', 'last_name', 'email']
        
class CommentPostingForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        