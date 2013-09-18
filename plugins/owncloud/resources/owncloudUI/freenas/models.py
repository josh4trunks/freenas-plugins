from django.db import models


class Owncloud(models.Model):
    """
    Django model describing every tunable setting for ownCloud
    """

    enable = models.BooleanField(default=False)
