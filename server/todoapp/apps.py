from django.apps import AppConfig

class TodoappConfig(AppConfig):
    name = 'todoapp'
    def ready(self):
        import todoapp.api_sileo
