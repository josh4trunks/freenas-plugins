import hashlib
import json
import os
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

        rcconf = os.path.join(utils.sickbeard_etc_path, "rc.conf")
        with open(rcconf, "w") as f:
            if obj.enable:
                f.write('sickbeard_enable="YES"\n')

        os.system(os.path.join(utils.sickbeard_pbi_path, "tweak-rcconf"))
