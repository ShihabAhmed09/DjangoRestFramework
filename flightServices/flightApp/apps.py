from django.apps import AppConfig


class FlightappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'flightApp'

    def ready(self):
        import flightApp.signals
