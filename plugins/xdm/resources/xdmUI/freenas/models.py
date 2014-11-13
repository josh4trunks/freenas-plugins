import platform

from django.db import models


class XDM(models.Model):
    """
    Django model describing every tunable setting for xdm
    """

    enable = models.BooleanField(default=False)
