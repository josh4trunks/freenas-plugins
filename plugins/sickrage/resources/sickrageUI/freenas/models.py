import platform

from django.db import models


class SickRage(models.Model):
    """
    Django model describing every tunable setting for sickrage
    """

    enable = models.BooleanField(default=False)
