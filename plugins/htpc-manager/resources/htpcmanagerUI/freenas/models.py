import platform

from django.db import models


class HTPCManager(models.Model):
    """
    Django model describing every tunable setting for htpcmanager
    """

    enable = models.BooleanField(default=False)
