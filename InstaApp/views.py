from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from .forms import  CreateUserForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Profile,Image
from .forms import ProfileForm,ImageForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
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
        profile=Profile.objects.get(id=user_id)
        images = request.user.profile.images.all()
        contex = {'profile':profile, 'images':images}
        return render(request, 'profile.html', contex)
    
@login_required(login_url='loginPage')
def profileUpdates(request):
    current_user=request.user
    profile = Profile.objects.filter(id=current_user.id).first()
    if request.method == 'POST':
        profileform = ProfileForm(request.POST,request.FILES,instance=profile)
        if  profileform.is_valid:
            profileform.save(commit=False)
            profileform.user=request.user
            profileform.save()
            return redirect('index')
    else:
        form=ProfileForm(instance=profile)
    return render(request,'addProfile.html',{'form':form})

@login_required(login_url='loginPage')
def addNewPost(request):
    user = Profile.objects.get(user=request.user)
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.save(commit=False)
            data.profile = user
            data.user=request.user.profile
            data.save()
            return redirect('index')
        else:
            form=ImageForm()
    
    return render(request, 'addNewImage.html', {'form':ImageForm,})
    # if request.method=='POST':
    #     form=ImageForm(request.POST,request.FILES)
    #     if form.is_valid():
    #         image=form.save(commit=False)
    #         image.user=request.user.profile
    #         image.save()
    #         return HttpResponseRedirect(request.path_info)
    # else:
    #     form=ImageForm()
    # return render(request,'addNewImage.html',{'form':form})
    
    def search_results(request):    
        if "users" in request.GET and request.GET["users"]:
            search_term = request.GET.get("users")
            searched_accounts = Post.search_user(search_term)
            message = f"{search_term}"

            return render(request, 'search.html',{"message":message,"users": searched_accounts})

        else:
            message = "You haven't searched for any user"
            return render(request, 'search.html',{"message":message})