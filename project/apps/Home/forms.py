from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User


class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = User
        field = ["username", "password"]
        widgets = {
            "username": forms.TextInput(),
            "password": forms.PasswordInput(),
        }
