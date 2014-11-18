from subprocess import Popen, PIPE
import hashlib
import json
import pwd
import urllib

from django.utils.translation import ugettext_lazy as _

from dojango import forms
from syncthingUI.freenas import models, utils


class SyncthingForm(forms.ModelForm):

    class Meta:
        model = models.Syncthing
        exclude = (
            'enable',
            )

    def __init__(self, *args, **kwargs):
        self.jail_path = kwargs.pop('jail_path')
        super(SyncthingForm, self).__init__(*args, **kwargs)

    def save(self, *args, **kwargs):
        obj = super(SyncthingForm, self).save(*args, **kwargs)

        if obj.enable:
            Popen(["/usr/sbin/sysrc", "syncthing_enable=YES"],
                stdout=PIPE,
                stderr=PIPE)
        else:
            Popen(["/usr/sbin/sysrc", "syncthing_enable=NO"],
                stdout=PIPE,
                stderr=PIPE)
