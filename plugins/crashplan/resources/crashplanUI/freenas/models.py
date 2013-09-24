from django.db import models


class Crashplan(models.Model):
    """
    Django model describing every tunable setting for Crashplan
    """

    enable = models.BooleanField(default=False)
    lic_accepted = models.BooleanField(default=False)
