import hashlib
import json
import os
import pwd
import urllib

from django.utils.translation import ugettext_lazy as _

from dojango import forms
from syncthingUI.freenas import models, utils


class SyncthingForm(forms.ModelForm):

    class Meta:
        model = models.Syncthing
        exclude = ('enable',)

    def __init__(self, *args, **kwargs):
        self.jail_path = kwargs.pop('jail_path')
        super(SyncthingForm, self).__init__(*args, **kwargs)

    def save(self, *args, **kwargs):
        obj = super(SyncthingForm, self).save(*args, **kwargs)

        rcconf = os.path.join(utils.syncthing_etc_path, "rc.conf")
        with open(rcconf, "w") as f:
            if obj.enable:
                f.write('syncthing_enable="YES"\n')

        os.system(os.path.join(utils.syncthing_pbi_path, "tweak-rcconf"))
