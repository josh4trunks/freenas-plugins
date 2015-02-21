from subprocess import Popen, PIPE
import hashlib
import json
import pwd
import urllib

from django.utils.translation import ugettext_lazy as _

from dojango import forms
from sickbeardUI.freenas import models, utils


class SickBeardForm(forms.ModelForm):

    class Meta:
        model = models.SickBeard
        exclude = (
            'enable',
            )

    def __init__(self, *args, **kwargs):
        self.jail_path = kwargs.pop('jail_path')
        super(SickBeardForm, self).__init__(*args, **kwargs)

    def save(self, *args, **kwargs):
        obj = super(SickBeardForm, self).save(*args, **kwargs)

        if obj.enable:
            Popen(["/usr/sbin/sysrc", "sickbeard_enable=YES"],
                stdout=PIPE,
                stderr=PIPE)
        else:
            Popen(["/usr/sbin/sysrc", "sickbeard_enable=NO"],
                stdout=PIPE,
                stderr=PIPE)
