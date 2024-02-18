from .models import User
from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, \
UserChangeForm


# Create your models here.
class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'id': 'username',
            'placeholder': "Username",
            'type': "text",
            'required': ""}
    ))

    password = forms.CharField(widget=forms.TextInput(
        attrs={'id': 'password',
            'placeholder': "Password",
            'type': "password",
            'required': ""}
    ))

    class Meta:
        models = User
        fields = ('username', 'password')


class RegisterForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'id': 'username',
            'placeholder': "Имя пользователя",
            'type': "text"
        }))
    first_name = forms.CharField(widget=forms.TextInput(
        attrs={
            'id': 'username',
            'placeholder': "Имя",
            'type': "text"
        }))
    last_name = forms.CharField(widget=forms.TextInput(
        attrs={
            'id': 'username',
            'placeholder': "Фамилия",
            'type': "text"
        }))
    date_of_birth = forms.CharField(widget=forms.TextInput(
        attrs={
            'id': 'username',
            'placeholder': "Дата рождения",
            'type': "text"
        }))
    brief_information = forms.CharField(required=False ,widget=forms.TextInput(
        attrs={
            'id': 'username',
            'placeholder': "Описание",
            'type': "text"
        }))
    password1 = password2 = forms.CharField(widget=forms.TextInput(
        attrs={
            'id': 'password',
            'placeholder': "Пароль",
            'type': "password"
        }))
    
    class Meta:
        model = User
        fields = ('image','username', 'first_name', 'last_name', \
                'date_of_birth', 'gender', 'brief_information', \
                'password1', 'password2')
        

class UserProfile(UserChangeForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'date_of_birth', \
                'gender', 'brief_information')