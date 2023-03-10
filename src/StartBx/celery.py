import os

from celery import Celery

'''
Django adds tasks to Redis; Redis feeds tasks to Celery
'''

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'StartBx.settings')

app = Celery('StartBx', backend="redis", broker="redis://localhost:6379")

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

#tells celery how to find redis
app.conf.broker_url = 'redis://localhost:6379'

# Load task modules from all registered Django apps.
app.autodiscover_tasks()

