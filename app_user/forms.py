from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from django.contrib.auth.models import User
from .models import *

class LogInForm(AuthenticationForm):
    class Meta:
        fields = [
            'username',
            'password',
        ]

class UserRegistrationForm(UserCreationForm):
    day_of_birth = forms.DateField(widget=forms.DateInput(format="%Y-%m-%d", attrs={"type": "date"}),input_formats=["%Y-%m-%d"]) 
    class Meta():
        model = User
        fields = ['first_name','last_name','day_of_birth','username', 'email', 'password1','password2']