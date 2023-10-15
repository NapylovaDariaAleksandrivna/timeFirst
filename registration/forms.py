from .models import Pepople
from django.contrib.auth.forms import UserCreationForm
from django import forms
class RegisterForm(UserCreationForm):
    password1=forms.PasswordInput()
    password2=forms.PasswordInput()
    
    class Meta:
        model = Pepople
        fields = ['username', 'institute', 'group','password1', 'password2']


class LoginForm(forms.Form):
    username = forms.CharField(max_length=65)
    password = forms.CharField(max_length=65, widget=forms.PasswordInput)