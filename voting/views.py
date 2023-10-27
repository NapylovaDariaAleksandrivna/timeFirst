from django.shortcuts import render, redirect
from .forms import VoitingT, VoitingS
from .models import V, CandidateTeacher, CandidateStudent
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
                formT = VoitingT()
                formS = VoitingS()
                return render(request, 'homeAfter.html', {'formT': formT, 'formS': formS, 'nominationsT':objT, 'nominationsS':objS})
            if request.method == 'POST':
                formT = VoitingT(request.POST)
                formS = VoitingS(request.POST)
                if formT.is_valid() and formS.is_valid():
                    form=V()
                    form.nomination1=formT.cleaned_data['nomination1']
                    form.nomination2=formT.cleaned_data['nomination2']
                    form.nomination3=formT.cleaned_data['nomination3']
                    form.nomination4=formT.cleaned_data['nomination4']
                    form.nomination5=formT.cleaned_data['nomination5']

                    form.nomination6=formS.cleaned_data['nomination6']
                    form.nomination7=formS.cleaned_data['nomination7']
                    form.nomination8=formS.cleaned_data['nomination8']
                    form.nomination9=formS.cleaned_data['nomination9']
                    form.nomination10=formS.cleaned_data['nomination10']
                    form.nomination11=formS.cleaned_data['nomination11']
                    form.nomination12=formS.cleaned_data['nomination12']
                    form.save()
                    request.user.setFlag(form)
                    request.user.save()
                    return render(request, 'Last.html')
                else:
                    messages.success(request, 'Ошибка')
                    return render(request, 'homeAfter.html', {'formT': formT, 'formS': formS, 'nominationsT':objT, 'nominationsS':objS})
     else:
        return render(request, 'homeBefore.html')

def voiting (request):
    if request.user.is_authenticated:
        objT=vars(request.user.flag)

        obj=[]
        i=0
        for n in objT:
            if (i>1):
                if (i<7):
                    obj.append(CandidateTeacher.objects.get(pk=objT[n]))
                else:
                    obj.append(CandidateStudent.objects.get(pk=objT[n]))
            i+=1        
        return render(request, 'Voiting.html', {'obj':obj})
    else:
        return render(request, 'homeBefore.html')