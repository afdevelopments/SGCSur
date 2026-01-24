from dataclasses import field
from datetime import datetime
from django import forms
from django.contrib.auth.forms import AuthenticationForm, UsernameField, UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm, DateInput
from django.shortcuts import render
from django.core.exceptions import ValidationError

from .models import Carreras, Empresa, Contacto, Convenio


class UpperCaseMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        exempt_fields = getattr(self, 'uppercase_exempt_fields', [])
        lowercase_fields = getattr(self, 'lowercase_fields', [])
        
        for field_name, field in self.fields.items():
            if field_name in exempt_fields or field_name in lowercase_fields:
                continue
            if isinstance(field.widget, (forms.TextInput, forms.Textarea)):
                field.widget.attrs.update({'style': 'text-transform: uppercase;'})

    def clean(self):
        cleaned_data = super().clean()
        if not cleaned_data:
            return cleaned_data
        
        exempt_fields = getattr(self, 'uppercase_exempt_fields', [])
        lowercase_fields = getattr(self, 'lowercase_fields', [])
            
        for name, value in cleaned_data.items():
            if isinstance(value, str):
                if name in lowercase_fields:
                    cleaned_data[name] = value.lower()
                elif name not in exempt_fields:
                    cleaned_data[name] = value.upper()
        return cleaned_data


# Para cambiar el label del usuario y contraseña
class CustomAuthenticationForm(AuthenticationForm):
    username = UsernameField(label='Usuario', widget=forms.TextInput())
    password = forms.CharField(label="Contraseña", widget=forms.PasswordInput())


# Formulario de crear usuarios.
class RegistroForm(UserCreationForm):
    username = UsernameField(label='Usuario', widget=forms.TextInput())
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirmar contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


# Formulario de añadir / modificar carrera
class CarreraForm(UpperCaseMixin, ModelForm):
    nombreCarrera = forms.CharField(max_length=50, label="Nombre de la carrera")
    divisionesMenu = [
        ("Ciencias Sociales y Humanidades", "Ciencias Sociales y Humanidades"),
        ("Ciencias Exactas, Naturales y Tecnológicas", "Ciencias Exactas, Naturales y Tecnológicas"),
        ("Ciencias de la Salud", "Ciencias de la Salud"),
    ]
    divisionCarrera = forms.CharField(max_length=100, label="División de la carrera", widget=forms.Select(choices=divisionesMenu))

    class Meta:
        model = Carreras
        fields = ['nombreCarrera', 'divisionCarrera']


# Formulario de añadir / modificar empresa
class EmpresaForm(UpperCaseMixin, ModelForm):
    razonSocial = forms.CharField(max_length=200, label="Razón social de la empresa (Nombre legal)")
    nombre = forms.CharField(max_length=200, label="Nombre conocido de la empresa", required=False)
    rfc = forms.CharField(max_length=13, label="RFC de la empresa")
    giro = forms.CharField(max_length=50, label="Giro de la empresa")
    pais = forms.CharField(label="Pais", widget=forms.widgets.Select(attrs={'onchange': "print_state('state',this.selectedIndex);", 'id': 'country', 'name': 'country'}))
    estado = forms.CharField(label="Estado", widget=forms.widgets.Select(attrs={'name': 'state', 'id': 'state'}))
    ciudad = forms.CharField(max_length=200, label="Ciudad")
    colonia = forms.CharField(max_length=200, label="Colonia")
    calle = forms.CharField(max_length=200, label="Calle")
    numero = forms.CharField(max_length=10, label="Número")
    numeroInterior = forms.CharField(max_length=10, label="Número interior", required=False)
    cp = forms.CharField(max_length=5, label="Código postal")
    sectoresMenu = [
        ("Público", "Público"),
        ("Privado", "Privado"),
        ("Social", "Social"),
        ("Educativo", "Educativo"),
    ]
    sectorEmpresa = forms.CharField(max_length=100, label="Sector de la empresa", widget=forms.Select(choices=sectoresMenu))

    class Meta:
        model = Empresa
        fields = ['razonSocial', 'nombre', 'rfc', 'giro', 'pais', 'estado', 'ciudad', 'colonia', 'calle', 'numero', 'numeroInterior', 'cp', 'sectorEmpresa']


# Formulario de añadir / modificar contacto
class ContactoForm(UpperCaseMixin, ModelForm):
    nombre = forms.CharField(max_length=50, label="Nombre del contacto")
    numTelefono = forms.CharField(max_length=15, label="Número de teléfono")
    idEmpresa = forms.ModelChoiceField(queryset=Empresa.objects.all(), label="Empresa")
    email = forms.EmailField(max_length=254, label="Correo electrónico")

    class Meta:
        model = Contacto
        fields = ['nombre', 'numTelefono', 'idEmpresa', 'email']
    
    lowercase_fields = ['email']


# Formulario de convenio
class ConvenioForm(UpperCaseMixin, ModelForm):
    idCarrera = forms.ModelChoiceField(queryset=Carreras.objects.all(), label="Carrera")
    inicioVigencia = forms.DateField(label="Vigente desde")
    finVigencia = forms.DateField(label="Vigente hasta")
    idEmpresa = forms.ModelChoiceField(queryset=Empresa.objects.all(), label="Empresa")
    observaciones = forms.CharField(widget=forms.Textarea, label="Observaciones", required=False)

    class Meta:
        model = Convenio
        fields = ['idCarrera', 'inicioVigencia', 'finVigencia', 'idEmpresa', 'observaciones']
        widgets = {
            'inicioVigencia': DateInput(format='%d/%m/%Y', attrs={'class': 'datepicker'}),
            'finVigencia': DateInput(format='%d/%m/%Y', attrs={'class': 'datepicker'}),
        }
    
    uppercase_exempt_fields = ['observaciones']


# Formulario para filtrado de reportes:
class ReporteConveniosForm(UpperCaseMixin, forms.Form):
    idCarrera = forms.ModelMultipleChoiceField(queryset=Carreras.objects.all(), required=False)
    idEmpresa = forms.ModelMultipleChoiceField(queryset=Empresa.objects.all(), required=False)
    fecha_inicio = forms.DateField(required=False)
    fecha_vigencia = forms.CharField(required=False)
    estado = forms.ChoiceField(
        choices=[('activo', 'Activo'), ('casi_expirado', 'Casi expirado'), ('expirado', 'Expirado')],
        required=False)
    incluir_contactos = forms.BooleanField(required=False, label="Incluir contactos")
    sectores = forms.MultipleChoiceField(choices=Empresa.sectores, required=False, label="Sectores")

    def clean_fecha_vigencia(self):
        fecha_vigencia = self.cleaned_data.get('fecha_vigencia')

        if not fecha_vigencia or fecha_vigencia == 'Todas las fechas':
            return None
        try:
            rango_fechas = fecha_vigencia.split(' - ')
            fecha_inicio = datetime.strptime(rango_fechas[0], '%d/%m/%Y')
            fecha_fin = datetime.strptime(rango_fechas[1], '%d/%m/%Y')
            result = f'{fecha_inicio:%Y-%m-%d} - {fecha_fin:%Y-%m-%d}'
            return result
        except (ValueError, IndexError):
            raise forms.ValidationError("El formato de fecha debe ser 'DD/MM/YYYY - DD/MM/YYYY'.")


class ReporteContactosForm(UpperCaseMixin, forms.Form):
    idEmpresa = forms.ModelMultipleChoiceField(queryset=Empresa.objects.all(), required=False)
    estado_convenio = forms.ChoiceField(
        choices=[('activo', 'Activo'), ('casi_expirado', 'Casi expirado'), ('expirado', 'Expirado'), ('sin_convenio', 'Sin convenio')],
        required=False,
        label="Estado del Convenio"
    )

