from django.shortcuts import render, redirect
from .forms import Voiting
from django.contrib import messages
# Create your views here.
def last(request):
    if request.user.is_authenticated:
        if (request.user.getFlag):
            return redirect('last')    
    return redirect('home')

from .models import CandidateStudent, CandidateTeacher, N_ns

def home (request):
     if request.user.is_authenticated:
        if request.user.getFlag():
            return render(request, 'Last.html')
        else:
            nominations = N_ns.objects.all()[0]
            obj=nominations.candidateteacher_set.all()
            nominations = N_ns.objects.all()[1]
            obj=nominations.candidateteacher_set.all()
            if request.method == 'GET':
                form = Voiting()
                return render(request, 'homeAfter.html', 
                              {'form': form,
                               'objT':obj})
            if request.method == 'POST':
                form =Voiting(request.POST)
                if form.is_valid():
                    return redirect('last')
                else:
                    messages.success(request, 'Ошибка')
                    return render(request, 'homeAfter.html', {'form': form})
     else:
        return render(request, 'homeBefore.html')