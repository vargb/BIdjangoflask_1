from django.apps import AppConfig
from djongo.database import connect

class DbappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'dbapp'

