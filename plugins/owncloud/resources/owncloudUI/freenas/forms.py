import hashlib
import json
import os
import pwd
import urllib

from django.utils.translation import ugettext_lazy as _

from dojango import forms
from owncloudUI.freenas import models, utils


class OwncloudForm(forms.ModelForm):

    class Meta:
        model = models.Owncloud
        exclude = (
            'enable',
        )

    def __init__(self, *args, **kwargs):
        self.jail_path = kwargs.pop('jail_path')
        super(OwncloudForm, self).__init__(*args, **kwargs)

    def save(self, *args, **kwargs):
        obj = super(OwncloudForm, self).save(*args, **kwargs)

        rcconf = os.path.join(utils.owncloud_etc_path, "rc.conf")
        with open(rcconf, "w") as f:
            if obj.enable:
                f.write('apache24_enable="YES"\n')

        os.system(os.path.join(utils.owncloud_pbi_path, "tweak-rcconf"))
