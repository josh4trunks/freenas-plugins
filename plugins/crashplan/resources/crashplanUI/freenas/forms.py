import hashlib
import json
import os
import pwd
import urllib

from django.utils.translation import ugettext_lazy as _

from dojango import forms
from crashplanUI.freenas import models, utils


class CrashplanForm(forms.ModelForm):

    class Meta:
        model = models.Crashplan
        exclude = (
            'enable',
        )

    def __init__(self, *args, **kwargs):
        self.jail_path = kwargs.pop('jail_path')
        super(CrashplanForm, self).__init__(*args, **kwargs)

    def clean(self):
        if self.instance.lic_accepted is False:
            self.errors['__all__'] = self.error_class([
                "Accept the license first"
            ])
            raise ValueError  #FIXME: workaround
        return self.cleaned_data

    def save(self, *args, **kwargs):
        obj = super(CrashplanForm, self).save(*args, **kwargs)

        rcconf = os.path.join(utils.crashplan_etc_path, "rc.conf")
        with open(rcconf, "w") as f:
            if obj.enable:
                f.write('crashplan_enable="YES"\n')

        os.system(os.path.join(utils.crashplan_pbi_path, "tweak-rcconf"))
