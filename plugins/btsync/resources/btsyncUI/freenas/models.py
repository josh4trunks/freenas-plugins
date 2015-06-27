import platform

from django.db import models


class BtSync(models.Model):
    """
    Django model describing every tunable setting for btsync
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
    config_refresh_interval = models.IntegerField(
        verbose_name="Config Refresh Interval (seconds)",
        default=3600,
        )
    config_save_interval = models.IntegerField(
        verbose_name="Config Save Interval (seconds)",
        default=600,
        )
    disk_low_priority = models.BooleanField(
        verbose_name="Disk Low Priority",
        default=True,
        )
    external_port = models.IntegerField(
        verbose_name="External Port",
        default=0,
        )
    folder_rescan_interval = models.IntegerField(
        verbose_name="Folder Rescan Interval (seconds)",
        default=600,
        )
    lan_encrypt_data = models.BooleanField(
        verbose_name="Lan Encrypt Data",
        default=True,
        )
    log_size = models.IntegerField(
        verbose_name="Max. Log File Size (MB)",
        default=100,
        )
    max_file_size_diff_for_patching = models.IntegerField(
        verbose_name="Max. File Size Difference for Patching (MB)",
        default=1000,
        )
    max_file_size_for_versioning = models.IntegerField(
        verbose_name="Max. File Size for Versioning (MB)",
        default=1000,
        )
    peer_expiration_days = models.IntegerField(
        verbose_name="Peer Expiration (days)",
        default=7,
        )
    rate_limit_local_peers = models.BooleanField(
        verbose_name="Rate Limit Local Peers",
        default=False,
        )
    sync_max_time_diff = models.IntegerField(
        verbose_name="Max. Time Difference (seconds)",
        default=600,
        )
    sync_trash_ttl = models.IntegerField(
        verbose_name="Trash Time to live (days)",
        default=30,
        )
