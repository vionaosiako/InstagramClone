from django.shortcuts import render,redirect
# from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .forms import  CreateUserForm
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
    contex = {}
    return render(request, 'auth/login.html', contex)
def index(request):
    return render(request, 'index.html')