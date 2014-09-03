import hashlib
import json
import os
import pwd
import urllib

from django.utils.translation import ugettext_lazy as _

from dojango import forms
from pydioUI.freenas import models, utils


class PydioForm(forms.ModelForm):

    class Meta:
        model = models.Pydio
        exclude = (
            'enable',
        )

    def __init__(self, *args, **kwargs):
        self.jail_path = kwargs.pop('jail_path')
        super(PydioForm, self).__init__(*args, **kwargs)

    def save(self, *args, **kwargs):
        obj = super(PydioForm, self).save(*args, **kwargs)

        rcconf = os.path.join(utils.pydio_etc_path, "rc.conf")
        with open(rcconf, "w") as f:
            if obj.enable:
                f.write('apache24_enable="YES"\n')

        os.system(os.path.join(utils.pydio_pbi_path, "tweak-rcconf"))
