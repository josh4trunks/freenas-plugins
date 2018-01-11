from django.db import models


class XMRig(models.Model):
    """
    Django model describing every tunable setting for xmrig
    """

    enable = models.BooleanField(default=False)
    algo = models.CharField(
        verbose_name="Algorithm",
        default="cryptonight",
        max_length=120,
        choices=(
            ('cryptonight', 'CryptoNight'),
            ('cryptonight-lite', 'CryptoNight-Lite'),
        ),
        )
    url = models.CharField(
        verbose_name="URL of Mining Pool",
        max_length=500,
        default="pool.minemonero.pro:5555",
        )
    user = models.CharField(
        verbose_name="Username for Mining Pool",
        max_length=500,
        blank=True,
        )
    password = models.CharField(
        verbose_name="Password for Mining Pool",
        max_length=500,
        default="x",
        )
    keepalive = models.BooleanField(
        verbose_name="Keep-Alive",
        default=True,
        )
    nicehash = models.BooleanField(
        verbose_name="NiceHash/XMRig-Proxy support",
        default=False,
        )
    av = models.IntegerField(
        verbose_name="Algorithm Variation",
        default=0,
        choices=(
            (0, 'Auto Select'),
            (1, 'Hardware AES'),
            (2, 'Hardware AES Low Power Mode'),
            (3, 'Software AES'),
            (4, 'Software AES Low Power Mode'),
        ),
        )
    threads = models.IntegerField(
        verbose_name="Threads",
        blank=True,
        null=True,
        )
    safe = models.BooleanField(
        verbose_name="Safely Adjust Settings",
        default=False,
        )
    cpu_affinity = models.CharField(
        verbose_name="CPU Affinity",
        max_length=120,
        blank=True,
        null=True,
        )
    max_cpu_usage = models.IntegerField(
        verbose_name="Max CPU Usage (%)",
        default=75,
        )
    cpu_priority = models.IntegerField(
        verbose_name="Process Priority",
        blank=True,
        null=True,
        choices=(
            (0, '0 - Idle'),
            (1, '1'),
            (2, '2 - Normal'),
            (3, '3'),
            (4, '4'),
            (5, '5 - Highest'),
        ),
        )
    donate_level = models.IntegerField(
        verbose_name="Donate Level (%)",
        default=5,
        )
    port = models.IntegerField(
        verbose_name="API Port",
        default=0,
        )
    access_token = models.CharField(
        verbose_name="API Access Token",
        max_length=500,
        blank=True,
        null=True,
        )
    worker_id = models.CharField(
        verbose_name="API Custom Worker-Id",
        max_length=500,
        blank=True,
        null=True,
        )
