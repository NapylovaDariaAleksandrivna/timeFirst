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
            'email': forms.TextInput(attrs={'placeholder': 'Почта'}),
            'username': forms.TextInput(attrs={'placeholder': 'Фамилия Имя Отчество','autocomplete': 'off'}),
            'password1': forms.PasswordInput(attrs={'placeholder': 'Пароль','autocomplete': 'off'}),
            'password2': forms.PasswordInput(attrs={'placeholder': 'Повторите пароль','autocomplete': 'off'}),
        }
    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget = forms.PasswordInput(attrs={'placeholder': 'Пароль','autocomplete': 'off'})
        self.fields['password2'].widget = forms.PasswordInput(attrs={ 'placeholder': 'Повторите пароль','autocomplete': 'off'})
    



class LoginForm(forms.Form):
    email = forms.CharField(max_length=65)
    password = forms.CharField(max_length=65)
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget = forms.EmailInput(attrs={'placeholder': 'Почта','autocomplete': 'off'})
        self.fields['password'].widget = forms.PasswordInput(attrs={ 'placeholder': 'Повторите','autocomplete': 'off'})