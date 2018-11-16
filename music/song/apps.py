from django.apps import AppConfig


class AlbumConfig(AppConfig):
    name = 'song'
    def ready(self):
        import song.signals