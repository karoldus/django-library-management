from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=50) # Required
    last_name = forms.CharField(max_length=50) # Required

    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "email", "password1", "password2"] # username, password1, password2 są wbudowane