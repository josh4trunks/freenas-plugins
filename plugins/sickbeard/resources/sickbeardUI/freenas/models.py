import platform

from django.db import models


class SickBeard(models.Model):
    """
    Django model describing every tunable setting for sickbeard
    """

    enable = models.BooleanField(default=False)
