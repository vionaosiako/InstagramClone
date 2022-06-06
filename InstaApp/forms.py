from django.contrib.auth.forms import UserCreationForm
from .models import Profile,Image,Comment
from django.forms import ModelForm,widgets
from django import forms
from django.contrib.auth.models import User
from django.core.files.images import get_image_dimensions

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email','username','password1','password2']
        
class ProfileForm(ModelForm):
	class Meta:
		model = Profile
		exclude = ['user']
		widgets = {
            'fullname': forms.TextInput(attrs={'class':'form-control'}),
            'bio': forms.Textarea(attrs={'class':'form-control'}),
        }


class ImageForm(ModelForm):
	class Meta:
		model = Image
		fields = ('image', 'name', 'caption')
		# exclude = ['user']
		# fields = '__all__'
		widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'caption': forms.Textarea(attrs={'class':'form-control'}),
        }
		
class CommentForm(ModelForm):
    class Meta:
        model=Comment
        fields =('comments',)
        widgets = {
            'comments': forms.TextInput(attrs={'class':'form-control'}),
        }
        