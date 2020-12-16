import os
from django.apps import AppConfig

class DjangoldpConfig(AppConfig):
    name = 'djangoldp'

    def ready(self):
        self.auto_register_model_admin()
        self.start_activity_queue()

    def start_activity_queue(self):
        from djangoldp.activities.services import ActivityQueueService
        if os.environ.get('RUN_MAIN') is not None:
            ActivityQueueService.start()

    def auto_register_model_admin(self):
        '''
        Automatically registers Model subclasses in the admin panel (which have not already been added manually)
        '''
        from importlib import import_module

        from django.conf import settings
        from django.contrib import admin
        from djangoldp.admin import DjangoLDPAdmin
        from djangoldp.models import Model

        for package in settings.DJANGOLDP_PACKAGES:
            try:
                import_module('{}.admin'.format(package))
            except ModuleNotFoundError:
                pass

        for package in settings.DJANGOLDP_PACKAGES:
            try:
                import_module('{}.models'.format(package))
            except ModuleNotFoundError:
                pass

        model_classes = {cls.__name__: cls for cls in Model.__subclasses__() if not Model.get_meta(cls, 'abstract', False)}

        for class_name in model_classes:
            model_class = model_classes[class_name]
            if not admin.site.is_registered(model_class):
                admin.site.register(model_class, DjangoLDPAdmin)
