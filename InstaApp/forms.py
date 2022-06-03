from django.contrib.auth.forms import UserCreationForm
# from .models import *
from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email','username','password1','password2']