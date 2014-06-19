import platform

from django.db import models


class BtSync(models.Model):
    """
    Django model describing every tunable setting for btsync
    """

    enable = models.BooleanField(default=False)
    webui_port = models.IntegerField(
        verbose_name="WebUI Port",
        default=8888,
        blank=True,
        )
    check_for_updates = models.BooleanField(
        verbose_name="Check for Updates",
        default=True,
        )
    disk_low_priority = models.BooleanField(
        verbose_name="Disk Low Priority",
        default=True,
        )
    external_port = models.IntegerField(
        verbose_name="External Port",
        default=0,
        blank=True,
        )
    folder_rescan_interval = models.IntegerField(
        verbose_name="Folder Rescan Interval (seconds)",
        default=600,
        blank=True,
        )
    lan_encrypt_data = models.BooleanField(
        verbose_name="Lan Encrypt Data",
        default=True,
        )
    log_size = models.IntegerField(
        verbose_name="Max. Log File Size (MB)",
        default=10,
        blank=True,
        )
    max_file_size_diff_for_patching = models.IntegerField(
        verbose_name="Max. File Size Difference for Patching (MB)",
        default=1000,
        blank=True,
        )
    max_file_size_for_versioning = models.IntegerField(
        verbose_name="Max. File Size for Versioning (MB)",
        default=1000,
        blank=True,
        )
    rate_limit_local_peers = models.BooleanField(
        verbose_name="Rate Limit Local Peers",
        default=False,
        )
    sync_max_time_diff = models.IntegerField(
        verbose_name="Max. Time Difference (seconds)",
        default=600,
        blank=True,
        )
    sync_trash_ttl = models.IntegerField(
        verbose_name="Trash Time to live (days)",
        default=30,
        blank=True,
        )
