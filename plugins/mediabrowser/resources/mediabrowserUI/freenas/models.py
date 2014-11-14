import platform

from django.db import models


class MediaBrowser(models.Model):
    """
    Django model describing every tunable setting for mediabrowser
    """

    enable = models.BooleanField(default=False)
