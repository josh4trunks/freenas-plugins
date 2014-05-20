import platform

from django.db import models


class Syncthing(models.Model):
    """
    Django model describing every tunable setting for syncthing
    """

    enable = models.BooleanField(default=False)
