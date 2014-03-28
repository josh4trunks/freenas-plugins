import hashlib
import json
import os
import pwd
import urllib

from django.utils.translation import ugettext_lazy as _

from dojango import forms
from mineosUI.freenas import models, utils


class MineOSForm(forms.ModelForm):

    class Meta:
        model = models.MineOS
        exclude = ('enable',)

    def __init__(self, *args, **kwargs):
        self.jail_path = kwargs.pop('jail_path')
        super(MineOSForm, self).__init__(*args, **kwargs)

    def save(self, *args, **kwargs):
        obj = super(MineOSForm, self).save(*args, **kwargs)

        rcconf = os.path.join(utils.mineos_etc_path, "rc.conf")
        with open(rcconf, "w") as f:
            if obj.enable:
                f.write('mineos_enable="YES"\n')

        os.system(os.path.join(utils.mineos_pbi_path, "tweak-rcconf"))
