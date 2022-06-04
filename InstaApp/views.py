from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from .forms import  CreateUserForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Profile
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
    return render(request, 'index.html')

@login_required(login_url='loginPage')
def profilePage(request,user_id):
    # if request.user == current_user:
        # profile=Profile.objects.all()
        profile=Profile.objects.get(id=user_id)
        contex = {'profile':profile}
        return render(request, 'profile.html', contex)
    # else:
    #     return render(request, 'auth/login.html')