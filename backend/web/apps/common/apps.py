from django.apps import AppConfig


class CommonConfig(AppConfig):
    name = 'common'
    def ready(self):
        try:
            import common.signals  # noqa F401
        except ImportError:
            pass