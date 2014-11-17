from subprocess import Popen, PIPE
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

        if obj.enable:
            Popen(["/usr/sbin/sysrc", "lazylibrarian_enable=YES"], stdout=PIPE, stderr=PIPE)
        else:
            Popen(["/usr/sbin/sysrc", "lazylibrarian_enable=NO"], stdout=PIPE, stderr=PIPE)
