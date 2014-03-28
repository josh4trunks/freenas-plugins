import platform

from django.db import models


class MineOS(models.Model):
    """
    Django model describing every tunable setting for mineos
    """

    enable = models.BooleanField(default=False)
