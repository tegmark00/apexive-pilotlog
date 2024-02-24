from django.apps import AppConfig


class PilotlogConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "pilotlog"

    class DFMeta:
        api_path = "pilotlog/"
