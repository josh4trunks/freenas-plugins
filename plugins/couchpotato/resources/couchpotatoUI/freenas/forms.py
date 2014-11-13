import hashlib
import json
import os
import pwd
import urllib

from django.utils.translation import ugettext_lazy as _

from dojango import forms
from couchpotatoUI.freenas import models, utils


class CouchPotatoForm(forms.ModelForm):

    class Meta:
        model = models.CouchPotato
        exclude = ('enable',)

    def __init__(self, *args, **kwargs):
        self.jail_path = kwargs.pop('jail_path')
        super(CouchPotatoForm, self).__init__(*args, **kwargs)

    def save(self, *args, **kwargs):
        obj = super(CouchPotatoForm, self).save(*args, **kwargs)

        rcconf = os.path.join(utils.couchpotato_etc_path, "rc.conf")
        with open(rcconf, "w") as f:
            if obj.enable:
                f.write('couchpotato_enable="YES"\n')

        os.system(os.path.join(utils.couchpotato_pbi_path, "tweak-rcconf"))
