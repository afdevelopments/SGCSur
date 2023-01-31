from dataclasses import field
from django import forms

from .models import *
from django.contrib.auth.forms import AuthenticationForm, UsernameField

class TaskForm(forms.ModelForm):
    title = forms.CharField(max_length=200, widget= forms.Textarea(attrs={'placeholder':'Enter new task here. . .'}))

    class Meta:
        model = Task
        fields = '__all__'

#Para cambiar el label de el usuario y contraseña
class CustomAuthenticationForm(AuthenticationForm):
    username = UsernameField(
        label='Usuario',
        widget=forms.TextInput()
    )
    password = forms.CharField(label="Contraseña", widget=forms.PasswordInput)

