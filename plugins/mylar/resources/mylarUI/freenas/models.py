import platform

from django.db import models


class Mylar(models.Model):
    """
    Django model describing every tunable setting for mylar
    """

    enable = models.BooleanField(default=False)
