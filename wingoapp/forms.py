from dataclasses import field
from django import forms
from django.forms import ModelForm, DateInput

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
    razonSocial = forms.CharField(max_length=200, label="Razón social de la empresa (Nombre legal)")
    nombre = forms.CharField(max_length=200, label="Nombre conocido de la empresa", required=False)
    rfc = forms.CharField(max_length=13, label="RFC de la empresa")
    giro = forms.CharField(max_length=50, label="Giro de la empresa")
    pais = forms.CharField(label="Pais de la empresa", widget=forms.widgets.Select(attrs={
        'onchange': "print_state('state',this.selectedIndex);", 'id': 'country', 'name': 'country'
    }))
    estado = forms.CharField(label="Estado de la empresa", widget=forms.widgets.Select(attrs={'name': 'state', 'id': 'state'}))
    ciudad = forms.CharField(max_length=200, label="Ciudad donde está ubicada la empresa")
    colonia = forms.CharField(max_length=200, label="Colonia donde está ubicada la empresa")
    calle = forms.CharField(max_length=200, label="Calle donde está ubicada la empresa")
    numero = forms.CharField(max_length=10, label="Número del local de la empresa")
    numeroInterior = forms.CharField(max_length=10, label="Número interior del local de la empresa", required=False)
    cp = forms.CharField(max_length=5, label="Código postal de la empresa")

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
        fields = ['razonSocial', 'nombre','rfc', 'giro', 'pais', 'estado', 'ciudad', 'colonia', 'calle', 'numero', 'numeroInterior', 'cp', 'sectorEmpresa']


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


class ConvenioForm(ModelForm):
    idCarrera = forms.ModelChoiceField(queryset=Carreras.objects.all(), label="Carrera")
    inicioVigencia = forms.DateField(widget=forms.DateInput(attrs=dict(type='date')), label="Vigente desde")
    finVigencia = forms.DateField(widget=forms.DateInput(attrs=dict(type='date')), label="Vigente hasta")
    idEmpresa = forms.ModelChoiceField(queryset=Empresa.objects.all(), label="Empresa")
    observaciones = forms.CharField( widget=forms.Textarea, label="Observaciones", required=False)

    # Class Meta para definir el modelo y los campos que se van a mostrar
    class Meta:
        model = Convenio
        fields = ['idCarrera', 'inicioVigencia', 'finVigencia', 'idEmpresa', 'observaciones']
        widgets = {
            'inicioVigencia': DateInput(),
            'finVigencia': DateInput(),
        }
