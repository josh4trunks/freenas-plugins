import platform

from django.db import models


class Resilio(models.Model):
    """
    Django model describing every tunable setting for resilio
    """

    enable = models.BooleanField(default=False)
    force_https = models.BooleanField(
        verbose_name="Enable SSL",
        default=False,
        )
    ssl_certificate = models.CharField(
        verbose_name="SSL Certificate",
        max_length=500,
        blank=True
        )
    ssl_private_key = models.CharField(
        verbose_name="SSL Private Key",
        max_length=500,
        blank=True
        )
    webui_port = models.IntegerField(
        verbose_name="WebUI Port",
        default=8888,
        )
