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
    cpu_affinity = models.CharField(
        verbose_name="CPU Affinity",
        max_length=120,
        blank=True,
        )
    donate_level = models.IntegerField(
        verbose_name="Donate Level",
        default=5,
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
    port = models.IntegerField(
        verbose_name="API Port",
        default=0,
        )
