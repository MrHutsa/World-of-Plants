from django.apps import AppConfig


class VentaConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'venta'
    # add this
    def ready(self):
        import venta.signals  # noqa