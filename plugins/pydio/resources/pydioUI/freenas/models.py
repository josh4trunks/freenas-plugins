from django.db import models


class Pydio(models.Model):
    """
    Django model describing every tunable setting for pydio
    """

    enable = models.BooleanField(default=False)
