from django import forms
from .models import N_nsS, N_nsT, V, N_nsE

class VoitingT(forms.ModelForm):
    nominations = N_nsT.objects.all()
    obj=[]
    for i in nominations:
        obj.append(i.candidateteacher_set.all())
    nomination1=forms.ModelChoiceField(queryset=obj[0], empty_label=nominations[0])
    nomination2=forms.ModelChoiceField(queryset=obj[1], empty_label=nominations[1])
    nomination3=forms.ModelChoiceField(queryset=obj[2], empty_label=nominations[2])
    nomination4=forms.ModelChoiceField(queryset=obj[3], empty_label=nominations[3])
    nomination5=forms.ModelChoiceField(queryset=obj[4], empty_label=nominations[4])
    class Meta:
        model=V
        fields = ['nomination1', 'nomination2', 'nomination3', 'nomination4','nomination5']
    def __init__(self, *args, **kwargs):
        super(VoitingT, self).__init__(*args, **kwargs)

        self.fields['nomination1'].label_from_instance = self.label_from_instance
        self.fields['nomination2'].label_from_instance = self.label_from_instance
        self.fields['nomination3'].label_from_instance = self.label_from_instance
        self.fields['nomination4'].label_from_instance = self.label_from_instance
        self.fields['nomination5'].label_from_instance = self.label_from_instance
    @staticmethod
    def label_from_instance(obj):
        return obj.second_name



class VoitingS(forms.ModelForm):
    nominations = N_nsS.objects.all()
    
    obj=[]
    for i in nominations:
        obj.append(i.candidatestudent_set.all())
    nomination6=forms.ModelChoiceField(queryset=obj[0], empty_label=nominations[0])
    nomination7=forms.ModelChoiceField(queryset=obj[1], empty_label=nominations[1])
    nomination8=forms.ModelChoiceField(queryset=obj[2], empty_label=nominations[2])
    nomination9=forms.ModelChoiceField(queryset=obj[3], empty_label=nominations[3])
    nomination10=forms.ModelChoiceField(queryset=obj[4], empty_label=nominations[4])
    nomination11=forms.ModelChoiceField(queryset=obj[5], empty_label=nominations[5])
    nomination12=forms.ModelChoiceField(queryset=obj[6], empty_label=nominations[6])
    class Meta:
        model=V
        fields = ['nomination6', 'nomination7', 'nomination8','nomination9', 'nomination10', 'nomination11', 'nomination12']
    def __init__(self, *args, **kwargs):
        super(VoitingS, self).__init__(*args, **kwargs)
        self.fields['nomination6'].label_from_instance = self.label_from_instance
        self.fields['nomination7'].label_from_instance = self.label_from_instance
        self.fields['nomination8'].label_from_instance = self.label_from_instance
        self.fields['nomination9'].label_from_instance = self.label_from_instance
        self.fields['nomination10'].label_from_instance = self.label_from_instance
        self.fields['nomination11'].label_from_instance = self.label_from_instance
        self.fields['nomination12'].label_from_instance = self.label_from_instance
    @staticmethod
    def label_from_instance(obj):
        return obj.second_name
    
    
class VoitingE(forms.ModelForm):
    nominations = N_nsE.objects.all()
    obj=[]
    for i in nominations:
        obj.append(i.candidateevent_set.all())
    nomination13=forms.ModelChoiceField(queryset=obj[0], empty_label=nominations[0])
    class Meta:
        model=V
        fields = ['nomination13']
    def __init__(self, *args, **kwargs):
        super(VoitingE, self).__init__(*args, **kwargs)
        self.fields['nomination13'].label_from_instance = self.label_from_instance
    @staticmethod
    def label_from_instance(obj):
        return obj.first_name