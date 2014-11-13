import platform

from django.db import models


class CouchPotato(models.Model):
    """
    Django model describing every tunable setting for couchpotato
    """

    enable = models.BooleanField(default=False)
