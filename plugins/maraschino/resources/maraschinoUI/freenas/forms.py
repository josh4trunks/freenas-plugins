import hashlib
import json
import os
import pwd
import urllib

from django.utils.translation import ugettext_lazy as _

from dojango import forms
from maraschinoUI.freenas import models, utils


class MaraschinoForm(forms.ModelForm):

    class Meta:
        model = models.Maraschino
        exclude = ('enable',)

    def __init__(self, *args, **kwargs):
        self.jail_path = kwargs.pop('jail_path')
        super(MaraschinoForm, self).__init__(*args, **kwargs)

    def save(self, *args, **kwargs):
        obj = super(MaraschinoForm, self).save(*args, **kwargs)

        rcconf = os.path.join(utils.maraschino_etc_path, "rc.conf")
        with open(rcconf, "w") as f:
            if obj.enable:
                f.write('maraschino_enable="YES"\n')

        os.system(os.path.join(utils.maraschino_pbi_path, "tweak-rcconf"))
