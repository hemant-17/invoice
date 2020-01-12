from django.apps import AppConfig


class DevalappersConfig(AppConfig):
    name = 'devalappers'
    def ready(self):
        import devalappers.mysignal
