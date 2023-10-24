from django.shortcuts import render, redirect
from .forms import Voiting
from django.contrib import messages
# Create your views here.
def last(request):
    if request.user.is_authenticated:
        if (request.user.getFlag):
            return redirect('last')    
    return redirect('home')

from .models import N_nsS, N_nsT

def home (request):
     if request.user.is_authenticated:
        if request.user.getFlag():
            return render(request, 'Last.html')
        else:
            nominations = N_nsT.objects.all()
            objT=[]
            for nom in nominations:
                objT.append({'name': nom.name, 'candidate': nom.candidateteacher_set.all()})
            nominations = N_nsS.objects.all()
            objS=[]
            for nom in nominations:
                objS.append({'name': nom.name, 'candidate': nom.candidatestudent_set.all()})
            if request.method == 'GET':
                form = Voiting()
                return render(request, 'homeAfter.html', {'form': form, 'nominationsT':objT, 'nominationsS':objS})
            if request.method == 'POST':
                form =Voiting(request.POST)
                if form.is_valid():
                    return redirect('last')
                else:
                    messages.success(request, 'Ошибка')
                    return render(request, 'homeAfter.html', {'form': form, 'nominationsT':objT, 'nominationsS':objS})
     else:
        return render(request, 'homeBefore.html')