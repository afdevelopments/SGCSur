from dataclasses import field
from django import forms
from django.forms import ModelForm

from .models import *
from django.contrib.auth.forms import AuthenticationForm, UsernameField
import pycountry
import gettext

español = gettext.translation('iso3166', pycountry.LOCALES_DIR, languages=['es'])
español.install()
_ = español.gettext


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


# Formulario de añadir / modificar carrera
class CarreraForm(ModelForm):
    nombreCarrera = forms.CharField(max_length=50, label="Nombre de la carrera")
    divisionesMenu = [
        ("Ciencias Sociales y Humanidades", "Ciencias Sociales y Humanidades"),
        ("Ciencias Exactas, Naturales y Tecnológicas", "Ciencias Exactas, Naturales y Tecnológicas"),
        ("Ciencias de la Salud", "Ciencias de la Salud"),
    ]
    divisionCarrera = forms.CharField(max_length=100, label="División de la carrera",
                                      widget=forms.Select(choices=divisionesMenu))

    # Class Meta para definir el modelo y los campos que se van a mostrar
    class Meta:
        model = Carreras
        fields = ['nombreCarrera', 'divisionCarrera']


# Formulario de añadir / modificar empresa
class EmpresaForm(ModelForm):
    razonSocial = forms.CharField(max_length=200, label="Nombre de la empresa")
    rfc = forms.CharField(max_length=13, label="RFC de la empresa")
    giro = forms.CharField(max_length=50, label="Giro de la empresa")
    pais = forms.CharField(label="Pais de la empresa", widget=forms.widgets.Select(attrs={
        'onchange': "print_state('state',this.selectedIndex);", 'id': 'country', 'name': 'country'
    }))
    estado = forms.CharField(label="Estado de la empresa", widget=forms.widgets.Select(attrs={'name': 'state', 'id': 'state'}))

    sectoresMenu = [
        ("Público", "Público"),
        ("Privado", "Privado"),
        ("Social", "Social"),
        ("Educativo", "Educativo"),
    ]
    sectorEmpresa = forms.CharField(max_length=100, label="Sector de la empresa",
                                    widget=forms.Select(choices=sectoresMenu))
# Class Meta para definir el modelo y los campos que se van a mostrar
    class Meta:
        model = Empresa
        fields = ['razonSocial', 'rfc', 'giro', 'pais', 'estado', 'sectorEmpresa']


# Formulario de añadir / modificar contacto
class ContactoForm(ModelForm):
    nombre = forms.CharField(max_length=50, label="Nombre del contacto")
    numTelefono = forms.CharField(max_length=10, label="Número de teléfono")
    idEmpresa = forms.ModelChoiceField(queryset=Empresa.objects.all(), label="Empresa")
    email = forms.EmailField(max_length=254, label="Correo electrónico")

    # Class Meta para definir el modelo y los campos que se van a mostrar
    class Meta:
        model = Contacto
        fields = ['nombre', 'numTelefono', 'idEmpresa', 'email']
