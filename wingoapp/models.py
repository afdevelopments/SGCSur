from django.core.validators import RegexValidator
from django.db import models
from django.utils.safestring import mark_safe
# Create your models here.


class Task(models.Model):
    title = models.CharField(max_length=200, null=False)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Empresa(models.Model):
    idEmpresa = models.AutoField(primary_key=True, verbose_name='ID del contacto')
    razonSocial = models.CharField(verbose_name='Razón social de la empresa', max_length=200,
                                   help_text="Ingrese la razón social de la empresa")
    nombre = models.CharField(verbose_name='Nombre conocido de la empresa', max_length=200,
                                   help_text="Ingrese el nombre conocido de la empresa")
    rfc = models.CharField(max_length=13, verbose_name='RFC',
                           help_text=mark_safe(
                               '12-13 caracteres <a href="https://www.sat.gob.mx/consultas/44083/consulta-tu'
                               '-informacion-fiscal"> consulta tu RFC</a>'),
                           #    validators=[RegexValidator(
                           #        regex='^([A-ZÃ&]{3,4}) ?(?:- ?)?(\d{2}(?:0[1-9]|1[0-2])(?:0[1-9]|[12]\d|3[01])) ?('
                           #              '?:- ?)?([A-Z\d]{2})([A\d])$',
                           #        message='El RFC deberá tener el formato que la Servicio de Administración Tributaria '
                           #                'valida',
                           #        code='invalid_RFC'), ]
                           )
    giro = models.CharField(verbose_name='Giro de la empresa', max_length=50,
                            help_text="Ingrese el giro de la empresa")
    pais = models.CharField(verbose_name='Pais de la empresa', max_length=50, help_text="Seleccione el pais",
                            null=False)
    estado = models.CharField(verbose_name='Estado de la empresa', max_length=50, help_text="Seleccione el estado",
                              null=False)
    ciudad = models.CharField(verbose_name='Ciudad de la empresa', max_length=200,
                                   help_text="Ingrese la ciudad donde está ubicada la empresa", null=False)
    colonia = models.CharField(verbose_name='Colonia de la empresa', max_length=200,
                                   help_text="Ingrese la colonia donde está ubicada la empresa", null=False)
    calle = models.CharField(verbose_name='Calle de la empresa', max_length=200,
                                   help_text="Ingrese la calle donde está ubicada la empresa", null=False)
    numero = models.CharField(verbose_name='Número de local de la empresa', max_length=10,
                                   help_text="Ingrese el número del local donde está ubicada la empresa", null=False)
    numeroInterior = models.CharField(verbose_name='Número interior de la empresa', max_length=10,
                                   help_text="Ingrese el número interior del local donde está ubicada la empresa", null=False)
    cp = models.CharField(max_length=5, verbose_name='Código postal de la empresa',
                                   help_text="Ingrese el código postal de la empresa", null=False)
    sectores = [
        ("Público", "Público"),
        ("Privado", "Privado"),
        ("Social", "Social"),
        ("Educativo", "Educativo"),
    ]
    sectorEmpresa = models.CharField(choices=sectores, default="Privado", max_length=20,
                                     help_text="Ingrese el sector", verbose_name='Sector de la empresa'
                                     )
    def __str__(self):
        return self.razonSocial


class Contacto(models.Model):
    idContacto = models.AutoField(primary_key=True, verbose_name='ID del contacto')
    nombre = models.CharField(verbose_name='Nombre del contacto', max_length=50,
                              help_text="Ingrese el nombre del contacto")
    numTelefono = models.CharField(max_length=10,
                                   help_text="Ingrese el número de teléfono del contacto", verbose_name='Número de '
                                                                                                        'Teléfono',
                                   #    validators=[RegexValidator(
                                   #        regex='(\(\d{3}\)[.-]?|\d{3}[.-]?)?\d{3}[.-]?\d{4}',
                                   #        message='El número es inválido.',
                                   #        code='invalid_number'), ]
                                   )
    idEmpresa = models.ForeignKey(Empresa, on_delete=models.CASCADE,
                                  help_text="Seleccione la empresa", verbose_name='Empresa'
                                  )
    email = models.EmailField(max_length=254, help_text="Introduzca el correo electrónico del contacto",
                              verbose_name="Correo Electrónico", default="")

    def __str__(self):
        return self.nombre


class Carreras(models.Model):
    idCarrera = models.AutoField(primary_key=True, verbose_name='ID de la carrera')
    nombreCarrera = models.CharField(verbose_name='Nombre de la carrera', max_length=50,
                                     help_text="Ingrese el nombre de la carrera")
    divisionesMenu = [
        ("Ciencias Sociales y Humanidades", "Ciencias Sociales y Humanidades"),
        ("Ciencias Exactas, Naturales y Tecnológicas", "Ciencias Exactas, Naturales y Tecnológicas"),
        ("Ciencias de la Salud", "Ciencias de la Salud"),
    ]
    divisionCarrera = models.CharField(choices=divisionesMenu, default="Ciencias Sociales y Humanidades",
                                       max_length=100,
                                       help_text="Ingrese la división de la carrera",
                                       verbose_name='División de la carrera'
                                       )

    def __str__(self):
        return self.nombreCarrera


class Convenio(models.Model):
    numConvenio = models.AutoField(primary_key=True, verbose_name='Número de convenio')
    idCarrera = models.ForeignKey(Carreras, on_delete=models.CASCADE, help_text="Seleccione la carrera",
                                  verbose_name='Carrera'
                                  )
    inicioVigencia = models.DateTimeField(auto_now=True)
    finVigencia = models.DateTimeField(auto_now=True)
    idEmpresa = models.ForeignKey(Empresa, on_delete=models.CASCADE,
                                  help_text="Seleccione la empresa", verbose_name='Empresa'
                                  )

    def __str__(self):
        return self.numConvenio
