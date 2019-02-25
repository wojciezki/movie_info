from __future__ import unicode_literals
from django.apps import AppConfig


class InfoConfig(AppConfig):
    name = 'info'

    def ready(self):
        from .models import Movie, Comment