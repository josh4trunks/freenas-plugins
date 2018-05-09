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
            ('cryptonight-heavy', 'CryptoNight-Heavy'),
        ),
        )
    variant = models.CharField(
        verbose_name="Algorithm PoW Variant",
        default="1",
        max_length=120,
        choices=(
            ('-1', 'Autodetect'),
            ('0', '0 - Original'),
            ('1', '1 - v7 / TurtleCoin'),
            ('xtl', 'Stellite'),
            ('ipbc', 'IPBC'),
        ),
        )
    url = models.CharField(
        verbose_name="URL of Mining Pool",
        default="proxy.fee.xmrig.com:9999",
        max_length=500,
        )
    user = models.CharField(
        verbose_name="Username for Mining Pool",
        default="YOUR_WALLET",
        max_length=500,
        blank=True,
        )
    password = models.CharField(
        verbose_name="Password for Mining Pool",
        default="x",
        max_length=500,
        )
    rig_id = models.CharField(
        verbose_name="Rig Identifier",
        max_length=120,
        blank=True,
        null=True,
        )
    user_agent = models.CharField(
        verbose_name="Custom User-Agent",
        max_length=120,
        blank=True,
        null=True,
        )
    nicehash = models.BooleanField(
        verbose_name="NiceHash/XMRig-Proxy support",
        default=False,
        )
    keepalive = models.BooleanField(
        verbose_name="Keep-Alive",
        default=True,                                                                                                                                                                                
        )
    av = models.IntegerField(
        verbose_name="Algorithm Variation",
        default=0,
        choices=(
            (0, 'Auto Select'),
            (1, 'Single Hash Mode'),
            (2, 'Double Hash Mode'),
            (3, 'Single Hash Mode (Software AES)'),
            (4, 'Double Hash Mode (Software AES)'),
            (5, 'Triple Hash Mode'),
            (6, 'Quard Hash Mode'),
            (7, 'Penta Hash Mode'),
            (8, 'Triple Hash Mode (Software AES)'),
            (9, 'Quard Hash Mode (Software AES)'),
            (10, 'Penta Hash Mode (Software AES)'),
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
    ipv6 = models.BooleanField(
        verbose_name="API Enable IPv6",
        default=False,
        )
    restricted = models.BooleanField(
        verbose_name="API Restrict Remote Configuration",
        default=False,
        )
