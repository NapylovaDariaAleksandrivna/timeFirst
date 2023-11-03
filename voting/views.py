from django.shortcuts import render, redirect
from .forms import VoitingT, VoitingS,VoitingE
from .models import V, CandidateTeacher, CandidateStudent,CandidateEvent
from django.contrib import messages
# Create your views here.
def last(request):
    if request.user.is_authenticated:
        if (request.user.getFlag):
            return redirect('last')    
    return redirect('home')

from .models import N_nsS, N_nsT,N_nsE

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
            nominations = N_nsE.objects.all()
            objE=[]
            for nom in nominations:
                objE.append({'name': nom.name, 'candidate': nom.candidateevent_set.all()})


            if request.method == 'GET':
                formT = VoitingT()
                formS = VoitingS()
                formE = VoitingE()
                return render(request, 'homeAfter.html', {'formT': formT, 'formS': formS,'formE': formE, 'nominationsT':objT, 'nominationsS':objS,'nominationsE':objE})
            if request.method == 'POST':
                formT = VoitingT(request.POST)
                formS = VoitingS(request.POST)
                formE = VoitingE(request.POST)
                if formT.is_valid() and formS.is_valid() and formE.is_valid():
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

                    form.nomination13=formE.cleaned_data['nomination13']
                    form.save()
                    request.user.setFlag(form)
                    request.user.save()
                    return render(request, 'Last.html')
                else:
                    messages.success(request, 'Ошибка')
                    return render(request, 'homeAfter.html', {'formT': formT, 'formS': formS,'formE': formE, 'nominationsT':objT, 'nominationsS':objS,  'nominationsE':objE})
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
                elif i<14:
                    obj.append(CandidateStudent.objects.get(pk=objT[n]))
                else:
                    obj.append(CandidateEvent.objects.get(pk=objT[n]))
            i+=1        
        return render(request, 'Voiting.html', {'obj':obj})
    else:
        return render(request, 'homeBefore.html')
    
from django.forms.models import model_to_dict
def for_admin(request):
    if request.user.is_superuser:
        voit = V.objects.all()
        dictionary={}
        for object in voit:
            i=0
            for pole in object.__dict__:
                if (i>1):
                    if (i<7):
                        people= (CandidateTeacher.objects.get(pk=object.__dict__[pole]))
                        nom=N_nsT.objects.get(pk=people.__dict__['nominations_id'])
                    elif i<14:
                        people= (CandidateStudent.objects.get(pk=object.__dict__[pole]))
                        nom=N_nsS.objects.get(pk=people.__dict__['nominations_id'])
                    else:
                        people= (CandidateEvent.objects.get(pk=object.__dict__[pole]))
                        nom=N_nsE.objects.get(pk=people.__dict__['nominations_id'])


                    peopleNom=model_to_dict(nom)['name']
                    peopleName=model_to_dict(people)['first_name']+" "+model_to_dict(people)['second_name']
                    pCopy=peopleName+" - "+peopleNom
                    if pCopy in dictionary:
                        dictionary[pCopy][2]+=1
                    else:
                        dictionary[pCopy]=[peopleNom,peopleName, 1]
                                    
                    
                i+=1
        return render(request, 'none.html', {'form': dictionary})
    return redirect('home')