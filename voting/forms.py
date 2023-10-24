from django import forms
from .models import N_nsS, N_nsT, V

class Voiting(forms.ModelForm):
    nominations = N_nsT.objects.all()
    obj=[]
    for i in nominations:
        obj.append(i.candidateteacher_set.all())
    nomination1=forms.ModelChoiceField(queryset=obj[0])
    nomination2=forms.ModelChoiceField(queryset=obj[1])
    nomination3=forms.ModelChoiceField(queryset=obj[2])
    nomination4=forms.ModelChoiceField(queryset=obj[3])
    nomination5=forms.ModelChoiceField(queryset=obj[4])
    
    nominations = N_nsS.objects.all()
    obj=[]
    for i in nominations:
        obj.append(i.candidatestudent_set.all())
    nomination6=forms.ModelChoiceField(queryset=obj[0])
    nomination7=forms.ModelChoiceField(queryset=obj[1])
    nomination8=forms.ModelChoiceField(queryset=obj[2])
    nomination9=forms.ModelChoiceField(queryset=obj[3])
    nomination10=forms.ModelChoiceField(queryset=obj[4])
    nomination11=forms.ModelChoiceField(queryset=obj[5])
    nomination12=forms.ModelChoiceField(queryset=obj[6])
    class Meta:
        model=V
        fields = ['nomination1', 'nomination2', 'nomination3', 'nomination4','nomination5', 'nomination6', 'nomination7', 'nomination8','nomination9', 'nomination10', 'nomination11', 'nomination12']