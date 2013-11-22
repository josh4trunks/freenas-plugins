import platform

from django.db import models


class Headphones(models.Model):
    """
    Django model describing every tunable setting for headphones
    """

    enable = models.BooleanField(default=False)
