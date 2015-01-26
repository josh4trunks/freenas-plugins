import platform

from django.db import models


class Sonarr(models.Model):
    """
    Django model describing every tunable setting for sonarr
    """

    enable = models.BooleanField(default=False)
