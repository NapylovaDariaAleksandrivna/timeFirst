from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth import login, authenticate, logout
# Create your views here.
def home (request):
    return render(request, 'home.html')

def sign_up(request):
    if request.method == 'GET':
        form = RegisterForm()
        return render(request, 'register.html', {'form': form})    
   
    if request.method == 'POST':
        form = RegisterForm(request.POST) 
        if form.is_valid():
            user = form.save()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'register.html', {'form': form})
        
from .forms import LoginForm


def sign_in(request):
    if request.user.is_authenticated:
            return redirect('home')
    if request.method == 'GET':
        form = LoginForm()
        return render(request, 'login.html', {'form': form})
    elif request.method == 'POST':
        form = LoginForm(request.POST)
        
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request,username=username,password=password)
            if user:
                login(request, user)
                return redirect('home')
        return render(request,'login.html',{'form': form})
    
def sign_out(request):
    logout(request)
    return redirect('login')        