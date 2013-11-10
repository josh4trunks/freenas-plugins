import platform

from django.db import models


class SABnzbd(models.Model):
    """
    Django model describing every tunable setting for sabnzbd
    """

    enable = models.BooleanField(default=False)
