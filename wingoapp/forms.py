from dataclasses import field
from django import forms

from .models import *
from django.contrib.auth.forms import AuthenticationForm, UsernameField


class TaskForm(forms.ModelForm):
    title = forms.CharField(max_length=200, widget=forms.Textarea(attrs={'placeholder': 'Enter new task here. . .'}))

    class Meta:
        model = Task
        fields = '__all__'


# Para cambiar el label del usuario y contraseña
class CustomAuthenticationForm(AuthenticationForm):
    username = UsernameField(
        label='Usuario',
        widget=forms.TextInput()
    )
    password = forms.CharField(label="Contraseña", widget=forms.PasswordInput)


# Formulario de añadir carrera
class CarreraForm(forms.Form):

    nombreCarrera = forms.CharField(max_length=50, label= "Nombre de la carrera")
    divisionesMenu = [
        ("Ciencias Sociales y Humanidades", "Ciencias Sociales y Humanidades"),
        ("Ciencias Exactas, Naturales y Tecnológicas", "Ciencias Exactas, Naturales y Tecnológicas"),
        ("Ciencias de la Salud", "Ciencias de la Salud"),
    ]
    divisionCarrera = forms.CharField(max_length=100, label="División de la carrera",
                                      widget=forms.Select(choices=divisionesMenu))

