import hashlib
import json
import os
import pwd
import urllib

from django.utils.translation import ugettext_lazy as _

from dojango import forms
from gamezUI.freenas import models, utils


class GamezForm(forms.ModelForm):

    class Meta:
        model = models.Gamez
        exclude = ('enable',)

    def __init__(self, *args, **kwargs):
        self.jail_path = kwargs.pop('jail_path')
        super(GamezForm, self).__init__(*args, **kwargs)

    def save(self, *args, **kwargs):
        obj = super(GamezForm, self).save(*args, **kwargs)

        rcconf = os.path.join(utils.gamez_etc_path, "rc.conf")
        with open(rcconf, "w") as f:
            if obj.enable:
                f.write('gamez_enable="YES"\n')

        os.system(os.path.join(utils.gamez_pbi_path, "tweak-rcconf"))
