from .models import Pepople
from django.contrib.auth.forms import UserCreationForm
from django import forms
class RegisterForm(UserCreationForm):
    password1=forms.PasswordInput()
    password2=forms.PasswordInput()
    
    class Meta:
        model = Pepople
        fields = ['username', 'email','password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Фамилия Имя Отчество'}),
            'email': forms.TextInput(attrs={'placeholder': 'Почта'}),
            'password1': forms.PasswordInput(attrs={'placeholder': 'Пароль'}),
            'password2': forms.PasswordInput(attrs={'placeholder': 'Повторите пароль'}),
        }
    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget = forms.PasswordInput(attrs={'placeholder': 'Пароль'})
        self.fields['password2'].widget = forms.PasswordInput(attrs={ 'placeholder': 'Повторите пароль'})
    



class LoginForm(forms.Form):
    email = forms.CharField(max_length=65)
    password = forms.CharField(max_length=65, widget=forms.PasswordInput)
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget = forms.TextInput(attrs={'placeholder': 'Почта'})
        self.fields['password'].widget = forms.PasswordInput(attrs={ 'placeholder': 'Повторите'})