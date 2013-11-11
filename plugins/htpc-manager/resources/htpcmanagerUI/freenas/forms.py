import hashlib
import json
import os
import pwd
import urllib

from django.utils.translation import ugettext_lazy as _

from dojango import forms
from htpcmanagerUI.freenas import models, utils


class HTPCManagerForm(forms.ModelForm):

    class Meta:
        model = models.HTPCManager
        exclude = ('enable',)

    def __init__(self, *args, **kwargs):
        self.jail_path = kwargs.pop('jail_path')
        super(HTPCManagerForm, self).__init__(*args, **kwargs)

    def save(self, *args, **kwargs):
        obj = super(HTPCManagerForm, self).save(*args, **kwargs)

        rcconf = os.path.join(utils.htpcmanager_etc_path, "rc.conf")
        with open(rcconf, "w") as f:
            if obj.enable:
                f.write('htpc_manager_enable="YES"\n')

        os.system(os.path.join(utils.htpcmanager_pbi_path, "tweak-rcconf"))
