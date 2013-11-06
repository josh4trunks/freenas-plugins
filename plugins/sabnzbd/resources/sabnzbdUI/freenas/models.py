import platform

from django.db import models


class Sabnzbd(models.Model):
    """
    Django model describing every tunable setting for sabnzbd
    """

    enable = models.BooleanField(default=False)

