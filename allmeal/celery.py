from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# Establece el entorno de Django para Celery
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'allmeal.settings')

# Crea una instancia de Celery
app = Celery('allmeal')

# Cargar la configuración de Celery desde settings.py
app.config_from_object('django.conf:settings', namespace='CELERY')

# Auto-discover tasks.py en las apps
app.autodiscover_tasks()