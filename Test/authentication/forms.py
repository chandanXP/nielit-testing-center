# authentication/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser


class SignupForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['name', 'enrollment_number', 'branch', 'phone', 'email', 'password1', 'password2']
