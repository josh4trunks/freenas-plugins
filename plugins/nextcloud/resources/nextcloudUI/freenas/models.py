from django.db import models


class Nextcloud(models.Model):
    """
    Django model describing every tunable setting for Nextcloud
    """

    enable = models.BooleanField(default=False)
