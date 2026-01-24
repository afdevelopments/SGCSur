from functools import reduce
from operator import or_
from datetime import datetime, timedelta
from django.db.models import Q
from django.utils import timezone
from .models import Convenio, Empresa
from .forms import ReporteConveniosForm

def filter_convenios(query_params):
    """
    Filters Convenio objects based on query parameters.
    Returns the filtered QuerySet and any error message.
    """
    lista_convenios = Convenio.objects.all().order_by('-inicioVigencia')
    error_message = None
    
    # Initialize form with data (even if empty) to use validation logic if needed,
    # or just manually extract since we are in a util.
    # Reusing the valid form logic is safest.
    form = ReporteConveniosForm(query_params)

    if form.is_valid():
        cleaned_data = form.cleaned_data
        idCarrera = cleaned_data.get('idCarrera')
        idEmpresa = cleaned_data.get('idEmpresa')
        fecha_inicio = cleaned_data.get('fecha_inicio')
        fecha_vigencia = cleaned_data.get('fecha_vigencia')
        estado = cleaned_data.get('estado')
        sectores = cleaned_data.get('sectores')

        q_objects = Q()

        if idCarrera:
            q_objects &= reduce(or_, [Q(idCarrera=carrera) for carrera in idCarrera])

        if idEmpresa:
            q_objects &= reduce(or_, [Q(idEmpresa=empresa) for empresa in idEmpresa])

        if sectores:
            q_objects &= Q(idEmpresa__sectorEmpresa__in=sectores)

        if fecha_inicio:
            q_objects &= Q(inicioVigencia__gte=fecha_inicio)

        if fecha_vigencia and fecha_vigencia != 'Todas las fechas':
            try:
                # Expecting 'YYYY-MM-DD - YYYY-MM-DD' from the form clean method
                # BUT the form clean method returns that format string.
                rango_fechas = fecha_vigencia.split(' - ')
                if len(rango_fechas) == 2:
                    fecha_inicio_vigencia = datetime.strptime(rango_fechas[0], '%Y-%m-%d')
                    fecha_fin_vigencia = datetime.strptime(rango_fechas[1], '%Y-%m-%d')
                    q_objects &= (Q(inicioVigencia__range=(fecha_inicio_vigencia, fecha_fin_vigencia)) |
                                    Q(finVigencia__range=(fecha_inicio_vigencia, fecha_fin_vigencia)))
            except ValueError:
                 error_message = "Error procesando el rango de fechas."
        
        # State filtering logic
        today = timezone.now().date()
        if estado == 'activo':
            q_objects &= Q(inicioVigencia__lte=today, finVigencia__gte=today)
        elif estado == 'casi_expirado':
            q_objects &= Q(finVigencia__gt=today,
                           finVigencia__lte=today + timedelta(days=30))
        elif estado == 'expirado':
            q_objects &= Q(finVigencia__lt=today)
            
        lista_convenios = lista_convenios.filter(q_objects)
    else:
        # If form is invalid, we might want to return errors or just all convenios
        # In the original view, if form is invalid (or GET without params), it returned all.
        pass

    return lista_convenios, form, error_message

def filter_contactos(query_params):
    """
    Filters Contacto objects based on query parameters.
    Returns the filtered QuerySet and the form.
    """
    from .models import Contacto
    from .forms import ReporteContactosForm

    lista_contactos = Contacto.objects.all().order_by('nombre')
    form = ReporteContactosForm(query_params)

    if form.is_valid():
        cleaned_data = form.cleaned_data
        idEmpresa = cleaned_data.get('idEmpresa')
        estado_convenio = cleaned_data.get('estado_convenio')

        q_objects = Q()

        if idEmpresa:
            q_objects &= Q(idEmpresa__in=idEmpresa)

        if estado_convenio:
            today = timezone.now().date()
            if estado_convenio == 'activo':
                companies_with_state = Convenio.objects.filter(
                    inicioVigencia__lte=today, finVigencia__gte=today
                ).values_list('idEmpresa', flat=True)
            elif estado_convenio == 'casi_expirado':
                companies_with_state = Convenio.objects.filter(
                    finVigencia__gt=today,
                    finVigencia__lte=today + timedelta(days=30)
                ).values_list('idEmpresa', flat=True)
            elif estado_convenio == 'expirado':
                companies_with_state = Convenio.objects.filter(
                    finVigencia__lt=today
                ).values_list('idEmpresa', flat=True)
            elif estado_convenio == 'sin_convenio':
                 companies_with_state = Empresa.objects.filter(convenio__isnull=True).values_list('idEmpresa', flat=True)
            else:
                companies_with_state = []
            
            q_objects &= Q(idEmpresa__in=companies_with_state)

        lista_contactos = lista_contactos.filter(q_objects)
    
    return lista_contactos, form
