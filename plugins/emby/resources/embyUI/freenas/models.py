import platform

from django.db import models


class Emby(models.Model):
    """
    Django model describing every tunable setting for emby
    """

    enable = models.BooleanField(default=False)
