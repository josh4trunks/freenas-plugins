import hashlib
import json
import os
import pwd
import urllib

from django.utils.translation import ugettext_lazy as _

from dojango import forms
from lazylibrarianUI.freenas import models, utils


class LazyLibrarianForm(forms.ModelForm):

    class Meta:
        model = models.LazyLibrarian
        exclude = ('enable',)

    def __init__(self, *args, **kwargs):
        self.jail_path = kwargs.pop('jail_path')
        super(LazyLibrarianForm, self).__init__(*args, **kwargs)

    def save(self, *args, **kwargs):
        obj = super(LazyLibrarianForm, self).save(*args, **kwargs)

        rcconf = os.path.join(utils.lazylibrarian_etc_path, "rc.conf")
        with open(rcconf, "w") as f:
            if obj.enable:
                f.write('lazylibrarian_enable="YES"\n')

        os.system(os.path.join(utils.lazylibrarian_pbi_path, "tweak-rcconf"))
