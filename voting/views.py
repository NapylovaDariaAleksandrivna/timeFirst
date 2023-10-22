from django.shortcuts import render, redirect

# Create your views here.
def last(request):
    if request.user.is_authenticated:
        if (request.user.getFlag):
            return redirect('last')
        else:
            return redirect('home')
    
    return redirect('home')