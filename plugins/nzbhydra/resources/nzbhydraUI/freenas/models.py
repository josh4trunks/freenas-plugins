import platform

from django.db import models


class NZBHydra(models.Model):
    """
    Django model describing every tunable setting for nzbhydra
    """

    enable = models.BooleanField(default=False)
