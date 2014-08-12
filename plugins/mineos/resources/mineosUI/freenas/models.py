import platform

from django.db import models


class MineOS(models.Model):
    """
    Django model describing every tunable setting for mineos
    """

    enable = models.BooleanField(default=False)
    mineos_ssl = models.BooleanField(
        verbose_name="Enable SSL",
        default=False,
        )
    mineos_cert = models.CharField(
        verbose_name="SSL Certificate",
        max_length=500,
        default='/etc/ssl/certs/mineos.crt',
        )
    mineos_key = models.CharField(
        verbose_name="SSL Private Key",
        max_length=500,
        default='/etc/ssl/certs/mineos.key',
        )
    mineos_port = models.IntegerField(
        verbose_name="WebUI Port",
        default=8080,
        )
    mineos_mask = models.BooleanField(
        verbose_name="Mask Password",
        default=False,
        )
    mineos_locale = models.CharField(
        verbose_name="Localization",
        default="en",
        choices=(
            ("en", 'English'),
            ("nl", 'Dutch'),
            ("ru", 'Russian'),
        ),
        max_length=120,
        )
    mineos_delay = models.IntegerField(
        verbose_name="Commit Delay (seconds)",
        default=10,
        )
    mineos_basedir = models.CharField(
        verbose_name="Base Directory",
        max_length=500,
        default='/var/games/minecraft',
        )
    mineos_log = models.CharField(
        verbose_name="Logfile",
        max_length=500,
        default='/var/log/mineos.log',
        )
