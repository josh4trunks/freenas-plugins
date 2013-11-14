import hashlib
import json
import os
import pwd
import urllib

from django.utils.translation import ugettext_lazy as _

from dojango import forms
from btsyncUI.freenas import models, utils


class BtSyncForm(forms.ModelForm):

    class Meta:
        model = models.BtSync
        exclude = ('enable',)

    def __init__(self, *args, **kwargs):
        self.jail_path = kwargs.pop('jail_path')
        super(BtSyncForm, self).__init__(*args, **kwargs)

    def save(self, *args, **kwargs):
        obj = super(BtSyncForm, self).save(*args, **kwargs)

        rcconf = os.path.join(utils.btsync_etc_path, "rc.conf")
        with open(rcconf, "w") as f:
            if obj.enable:
                f.write('btsync_enable="YES"\n')

        os.system(os.path.join(utils.btsync_pbi_path, "tweak-rcconf"))
