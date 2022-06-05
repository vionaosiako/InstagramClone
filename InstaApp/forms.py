from django.contrib.auth.forms import UserCreationForm
from .models import Profile,Image
from django.forms import ModelForm,widgets
from django import forms
from django.contrib.auth.models import User

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email','username','password1','password2']
        
class ProfileForm(ModelForm):
	class Meta:
		model = Profile
		fields = '__all__'
		# widgets={'name':forms.TextInput(attrs{class:'form-control'})}


class ImageForm(ModelForm):
	class Meta:
		model = Image
		fields = '__all__'