from django.apps import AppConfig


class ExperiencesAppConfig(AppConfig):
    name = 'backend.api.experiences'
    label = 'experiences'
    verbose_name = 'Experiences'

    def ready(self):
        import backend.api.experiences.signals

default_app_config = 'backend.api.experiences.ExperiencesAppConfig'
