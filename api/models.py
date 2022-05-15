from django.db import models

from api.mixins import EventDispatcherMixin


class Timestampable(models.Model):
    updated_at = models.DateTimeField('date updated', auto_now=True)
    created_at = models.DateTimeField('date created', auto_now_add=True)

    class Meta:
        abstract = True


class PayEvent(EventDispatcherMixin, Timestampable):
    data = models.JSONField(default=dict)
