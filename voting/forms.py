from .models import CandidateTeacher,CandidateStudent
from django import forms

class Voiting (forms.Form):
    N_ns=(
        ("n1","Самый стильный преподаватель"),
        ("n2","Самый прогрессивный преподаватель"),
        ("n3","Лучший лектор"),
        ("n4","Лучший наставник"),
        ('n5',"Преподаватель года")
    )
    
    Countries = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=N_ns)
