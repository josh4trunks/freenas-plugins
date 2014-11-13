import platform

from django.db import models


class LazyLibrarian(models.Model):
    """
    Django model describing every tunable setting for lazylibrarian
    """

    enable = models.BooleanField(default=False)
