from .models import App

from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver


@receiver(post_save, sender=App)
def createApp(sender, instance, created, **kwargs):
    if (created):   # if created
        app = instance
        if (app.hasDoc):
            app.docname = app.name.lower().replace(' ', '-')
            app.save()
        # update color field
        if (app.kind == 'App'):
            app.color = 'primary'
        if (app.kind == 'Design'):
            app.color = 'success'
        if (app.kind == 'API'):
            app.color = 'warning'
        if (app.kind == 'Server'):
            app.color = 'info'
        app.save()
