import platform

from django.db import models
from django.utils.translation import ugettext_lazy as _

class PlexMediaServer(models.Model):
    """
    Django model describing every tunable setting for plexmediaserver
    """

    enable = models.BooleanField(default=False)
    disable_remote_security = models.BooleanField(
        default=False,
        verbose_name=_("Disables security. May be needed for initial access.")
    )
