from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth import login, authenticate, logout
# Create your views here.
def home (request):
     if request.user.is_authenticated:
        if request.user.getFlag():
            return render(request, 'Last.html')
        else:
            return render(request, 'homeAfter.html')
     else:
        return render(request, 'homeBefore.html')

def sign_up(request):
    if request.user.is_authenticated:
            return redirect('home')
    if request.method == 'GET':
        form = RegisterForm()
        return render(request, 'Reg.html', {'form': form})    
   
    if request.method == 'POST':
        form = RegisterForm(request.POST) 
        if form.is_valid():
            user = form.save()
            user.save()
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('home')
        else:
            return render(request, 'Reg.html', {'form': form})
        
from .forms import LoginForm

from django.contrib import messages
def sign_in(request):
    if request.user.is_authenticated:
            return redirect('home')
    if request.method == 'GET':
        form = LoginForm()
        return render(request, 'login.html', {'form': form})
    elif request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user!=None:
                login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                return redirect('home')
            else:
                messages.success(request, 'Ошибка, проверьте почту и пароль')
        return render(request,'login.html',{'form': form})
    
def sign_out(request):
    logout(request)
    return redirect('login')        