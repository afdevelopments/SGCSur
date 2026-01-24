import random
from datetime import timedelta
from django.core.management.base import BaseCommand
from django.utils import timezone
from wingoapp.models import Carreras, Empresa, Contacto, Convenio

# Mock Data Arrays
CARRERA_NAMES = [
    ("Ingeniería en Telemática", "Ciencias Exactas, Naturales y Tecnológicas"),
    ("Licenciatura en Derecho", "Ciencias Sociales y Humanidades"),
    ("Licenciatura en Enfermería", "Ciencias de la Salud"),
    ("Ingeniería en Geofísica", "Ciencias Exactas, Naturales y Tecnológicas"),
    ("Licenciatura en Psicología", "Ciencias de la Salud"),
    ("Licenciatura en Administración", "Ciencias Sociales y Humanidades"),
]

EMPRESA_SUFFIXES = ["S.A. de C.V.", "S.C.", "A.C.", "LTD", "Inc."]
SECTORES = ["Privado", "Público", "Social", "Educativo"]
GIROS = ["Tecnología", "Salud", "Educación", "Construcción", "Legal", "Comercio"]

FIRST_NAMES = ["Juan", "María", "Pedro", "Ana", "Luis", "Sofía", "Carlos", "Fernanda", "Jorge", "Lucía"]
LAST_NAMES = ["Pérez", "García", "López", "González", "Rodríguez", "Martínez", "Hernández", "Díaz"]

STREETS = ["Av. Vallarta", "Calle Juárez", "Av. Chapultepec", "Calle Hidalgo", "Periférico Sur", "Av. México"]
CITIES = [("Guadalajara", "Jalisco"), ("Zapopan", "Jalisco"), ("Ciudad Guzmán", "Jalisco"), ("Monterrey", "Nuevo León"), ("CDMX", "CDMX")]

class Command(BaseCommand):
    help = 'Seeds the database with mock data for testing'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.WARNING('Deleting old data...'))
        Convenio.objects.all().delete()
        Contacto.objects.all().delete()
        Empresa.objects.all().delete()
        Carreras.objects.all().delete()

        self.stdout.write(self.style.SUCCESS('Creating Carreras...'))
        carreras_objs = []
        for name, division in CARRERA_NAMES:
            carrera = Carreras.objects.create(
                nombreCarrera=name,
                divisionCarrera=division
            )
            carreras_objs.append(carrera)

        self.stdout.write(self.style.SUCCESS('Creating Empresas...'))
        empresas_objs = []
        for i in range(15):
            razon_social = f"Empresa {i+1} {random.choice(EMPRESA_SUFFIXES)}"
            ciudad_info = random.choice(CITIES)
            empresa = Empresa.objects.create(
                razonSocial=razon_social,
                nombre=f"Empresa {i+1}",
                rfc=f"RFC{random.randint(1000000000, 9999999999)}",
                giro=random.choice(GIROS),
                pais="México",
                estado=ciudad_info[1],
                ciudad=ciudad_info[0],
                colonia=f"Colonia {random.choice(['Centro', 'Obrera', 'Americana', 'Moderna'])}",
                calle=random.choice(STREETS),
                numero=str(random.randint(1, 9999)),
                cp=str(random.randint(44000, 49000)),
                sectorEmpresa=random.choice(SECTORES)
            )
            empresas_objs.append(empresa)

        self.stdout.write(self.style.SUCCESS('Creating Contactos...'))
        for empresa in empresas_objs:
            # Create 1-3 contacts per company
            for _ in range(random.randint(1, 3)):
                first = random.choice(FIRST_NAMES)
                last = random.choice(LAST_NAMES)
                Contacto.objects.create(
                    nombre=f"{first} {last}",
                    numTelefono=f"33{random.randint(10000000, 99999999)}",
                    idEmpresa=empresa,
                    email=f"{first.lower()}.{last.lower()}@example.com"
                )

        self.stdout.write(self.style.SUCCESS('Creating Convenios...'))
        # Generate varied states
        # 1. Active
        self.create_convenios(10, carreras_objs, empresas_objs, "active")
        # 2. Expired
        self.create_convenios(10, carreras_objs, empresas_objs, "expired")
        # 3. Almost Expired
        self.create_convenios(5, carreras_objs, empresas_objs, "almost_expired")
        # 4. Not Started
        self.create_convenios(5, carreras_objs, empresas_objs, "future")

        self.stdout.write(self.style.SUCCESS('Database seeded successfully!'))

    def create_convenios(self, count, carreras, empresas, state):
        today = timezone.now().date()
        
        for _ in range(count):
            if state == "active":
                start_date = today - timedelta(days=random.randint(50, 200))
                end_date = today + timedelta(days=random.randint(50, 200))
            elif state == "expired":
                start_date = today - timedelta(days=random.randint(400, 600))
                end_date = today - timedelta(days=random.randint(10, 100))
            elif state == "almost_expired":
                start_date = today - timedelta(days=random.randint(200, 300))
                end_date = today + timedelta(days=random.randint(1, 29))
            elif state == "future":
                start_date = today + timedelta(days=random.randint(10, 50))
                end_date = today + timedelta(days=random.randint(100, 200))
            
            Convenio.objects.create(
                idCarrera=random.choice(carreras),
                idEmpresa=random.choice(empresas),
                inicioVigencia=start_date,
                finVigencia=end_date,
                observaciones=f"Convenio de prueba estado: {state}"
            )
