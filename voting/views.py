from django.shortcuts import render, redirect
from .forms import Voiting
from django.contrib import messages
# Create your views here.
def last(request):
    if request.user.is_authenticated:
        if (request.user.getFlag):
            return redirect('last')    
    return redirect('home')

from .models import CandidateStudent, CandidateTeacher

def home (request):
     if request.user.is_authenticated:
        if request.user.getFlag():
            return render(request, 'Last.html')
        else:
            objT=CandidateTeacher.objects.all()
            objS=CandidateStudent.objects.all()
            if request.method == 'GET':
                form = Voiting()
                return render(request, 'homeAfter.html', 
                              {'form': form,
                               'objT':objT,
                               'objS':objS})
            if request.method == 'POST':
                form =Voiting(request.POST)
                if form.is_valid():
                    return redirect('last')
                else:
                    messages.success(request, 'Ошибка')
                    return render(request, 'homeAfter.html', {'form': form},objT,objS)
     else:
        return render(request, 'homeBefore.html')