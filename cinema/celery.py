from __future__ import absolute_import, unicode_literals
import os

from cinema.settings import base
from celery import Celery




os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cinema.settings.dev')

app = Celery('cinema')

app.conf.update(timezone = 'Africa/Lagos')

app.config_from_object("cinema.settings.dev", namespace="CELERY"),

app.autodiscover_tasks(lambda: base.INSTALLED_APPS)

