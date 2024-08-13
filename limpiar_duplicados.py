import os
import django

# Configurar el entorno de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mi_proyecto.settings')
django.setup()

from mi_aplicacion.models import Persona

seen_emails = set()
duplicates = []

for persona in Persona.objects.all():
    if persona.email in seen_emails:
        duplicates.append(persona)
    else:
        seen_emails.add(persona.email)

for duplicate in duplicates:
    duplicate.delete()

print(f"Eliminados {len(duplicates)} registros duplicados.")
