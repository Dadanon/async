from django.apps import AppConfig


class ArticlesConfig(AppConfig):
    name = 'articles'

    def ready(self):
        try:
            import articles.signals
        except ImportError:
            pass
