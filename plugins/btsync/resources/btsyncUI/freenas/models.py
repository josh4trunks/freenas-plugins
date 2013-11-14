import platform

from django.db import models


class BtSync(models.Model):
    """
    Django model describing every tunable setting for btsync
    """

    enable = models.BooleanField(default=False)
