import hashlib
import json
import os
import pwd
import urllib

from django.utils.translation import ugettext_lazy as _

from dojango import forms
from xdmUI.freenas import models, utils


class XDMForm(forms.ModelForm):

    class Meta:
        model = models.XDM
        exclude = ('enable',)

    def __init__(self, *args, **kwargs):
        self.jail_path = kwargs.pop('jail_path')
        super(XDMForm, self).__init__(*args, **kwargs)

    def save(self, *args, **kwargs):
        obj = super(XDMForm, self).save(*args, **kwargs)

        rcconf = os.path.join(utils.xdm_etc_path, "rc.conf")
        with open(rcconf, "w") as f:
            if obj.enable:
                f.write('xdm_enable="YES"\n')

        os.system(os.path.join(utils.xdm_pbi_path, "tweak-rcconf"))
