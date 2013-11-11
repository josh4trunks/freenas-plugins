import hashlib
import json
import os
import pwd
import urllib

from django.utils.translation import ugettext_lazy as _

from dojango import forms
from mylarUI.freenas import models, utils


class MylarForm(forms.ModelForm):

    class Meta:
        model = models.Mylar
        exclude = ('enable',)

    def __init__(self, *args, **kwargs):
        self.jail_path = kwargs.pop('jail_path')
        super(MylarForm, self).__init__(*args, **kwargs)

    def save(self, *args, **kwargs):
        obj = super(MylarForm, self).save(*args, **kwargs)

        rcconf = os.path.join(utils.mylar_etc_path, "rc.conf")
        with open(rcconf, "w") as f:
            if obj.enable:
                f.write('mylar_enable="YES"\n')

        os.system(os.path.join(utils.mylar_pbi_path, "tweak-rcconf"))
