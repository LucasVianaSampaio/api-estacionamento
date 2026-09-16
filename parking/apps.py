from django.apps import AppConfig


class ParkingConfig(AppConfig):
    name = 'parking'
    verbose_name = 'Vaga'
    verbose_name_plural = 'Vagas'

    def ready(self):
        import parking.signals  # noqa: F401
