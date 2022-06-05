from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from .forms import  CreateUserForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Profile,Image
from .forms import ProfileForm,ImageForm
from django.contrib.auth.models import User
# Create your views here.
def registerPage(request):
    form =  CreateUserForm()
    contex = {'form':form}
    if request.method == 'POST':
        form= CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('loginPage')
    return render(request, 'auth/register.html', contex)
def loginPage(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.info(request, 'Username OR password is incorrect')
    contex = {}
    return render(request, 'auth/login.html', contex)

def logoutUser(request):
	logout(request)
	return redirect('loginPage')

@login_required(login_url='loginPage')
def index(request):
    images = Image.objects.all()
    contex={'images':images}
    return render(request, 'index.html',contex)

@login_required(login_url='loginPage')
def profilePage(request,user_id):
    # if request.user == current_user:
        # profile=Profile.objects.all()
        # images = Image.objects.filter(request.user)
        profile=Profile.objects.get(id=user_id)
        images = request.user.profile.images.all()
        contex = {'profile':profile, 'images':images}
        return render(request, 'profile.html', contex)
    
@login_required(login_url='loginPage')
def profileUpdates(request):

	form = ProfileForm()

	if request.method == 'POST':
		form = ProfileForm(request.POST)
		if form.is_valid():
			form.save()
			
	context = {'form':form}
	return render(request, 'addProfile.html', context)

@login_required(login_url='loginPage')
def addNewPost(request):

	form = ImageForm()

	if request.method == 'POST':
		form = ImageForm(request.POST)
		if form.is_valid():
			form.save()
			
	context = {'form':form}
	return render(request, 'addNewImage.html', context)
# def like(request, image_id):
#     image = Image.objects.get(id=image_id)
#     like = Likes.objects.filter(image = image ,user = request.user).count()
#     if like is None:
#         like = Likes()
#         like.image = image
#         like.user = request.user
#         like.save()
#     else:
#         like.delete()
#     return redirect('index')
# def like(request, image_id)
#     user = request.user
#     image = Image.objects.get(id=image_id)
#     liked = Liked.objects.filter(user=user, image=image).count()
    
#     if not liked:
#         like = Likes.objects.create(user=user,image=image)