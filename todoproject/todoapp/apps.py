from django.apps import AppConfig

class TodoappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'todoapp'
    verbose_name = 'Список желаний'
