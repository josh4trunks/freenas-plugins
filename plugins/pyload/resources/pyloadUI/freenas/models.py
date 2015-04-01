import platform

from django.db import models


class Maraschino(models.Model):
    """
    Django model describing every tunable setting for maraschino
    """

    enable = models.BooleanField(default=False)
