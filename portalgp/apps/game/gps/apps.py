from django.apps import AppConfig


class GpsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.game.gps"

    def ready(self):
        # Import and connect your signal handlers here
        from . import signals  # Import your signals.py file
