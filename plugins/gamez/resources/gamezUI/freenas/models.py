import platform

from django.db import models


class Gamez(models.Model):
    """
    Django model describing every tunable setting for gamez
    """

    enable = models.BooleanField(default=False)
