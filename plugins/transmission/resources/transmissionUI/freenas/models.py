import platform

from django.db import models


def download_dir():
    return '/usr/pbi/transmission-%s/etc/transmission/home/Downloads' % (
        platform.machine(),
        )


class Transmission(models.Model):
    """
    Django model describing every tunable setting for transmission
    """

    enable = models.BooleanField(default=False)
    watch_dir = models.CharField(
        verbose_name="Watch Directory",
        max_length=500,
        blank=True,
        )
    incomplete_dir = models.CharField(
        verbose_name="Incomplete Download Directory",
        max_length=500,
        blank=True,
        )
    script_torrent_done = models.CharField(
        verbose_name="Script Torrent Done",
        max_length=500,
        blank=True   
        )
    rpc_auth = models.BooleanField(
        verbose_name="RPC/WebUI Enabled",
        default=True,
        )
    rpc_port = models.IntegerField(
        verbose_name="RPC Port",
        default=9091,
        )
    rpc_auth_required = models.BooleanField(
        verbose_name="RPC Auth. Required",
        default=False,
        )
    rpc_username = models.CharField(
        verbose_name="RPC Username",
        max_length=120,
        blank=True,
        )
    rpc_password = models.CharField(
        verbose_name="RPC Password",
        max_length=120,
        blank=True,
        )
    rpc_whitelist = models.TextField(
        verbose_name="RPC Whitelist",
        blank=True,
        )
    utp = models.BooleanField(
        default=True,
        verbose_name=u"Micro Transport Protocol (\xb5TP)"
        )
    cache_size = models.IntegerField(
        verbose_name="Cache Size (MB)",
        default=4,
        )
    permissions = models.IntegerField(
        verbose_name="Downloaded Permissions",
        default=18,
        choices=(
            (63, '700'),
            (55, '710'),
            (54, '711'),
            (23, '750'),
            (22, '751'),
            (18, '755'),
            (7, '770'),
            (6, '771'),
            (2, '775'),
            (0, '777'),
        ),
        )
