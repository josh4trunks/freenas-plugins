import hashlib
import json
import os
import pwd
import urllib

from django.utils.translation import ugettext_lazy as _

from dojango import forms
from headphonesUI.freenas import models, utils


class HeadphonesForm(forms.ModelForm):

    class Meta:
        model = models.Headphones
        exclude = ('enable',)

    def __init__(self, *args, **kwargs):
        self.jail_path = kwargs.pop('jail_path')
        super(HeadphonesForm, self).__init__(*args, **kwargs)

    def save(self, *args, **kwargs):
        obj = super(HeadphonesForm, self).save(*args, **kwargs)

        rcconf = os.path.join(utils.headphones_etc_path, "rc.conf")
        with open(rcconf, "w") as f:
            if obj.enable:
                f.write('headphones_enable="YES"\n')

        os.system(os.path.join(utils.headphones_pbi_path, "tweak-rcconf"))
