from django.contrib import admin

from wingoapp.views import tasks
from .models import *

# Register your models here.

admin.site.register(Empresa)
admin.site.register(Contacto)
admin.site.register(Carreras)
admin.site.register(Convenio)