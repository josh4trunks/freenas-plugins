from subprocess import Popen, PIPE
import hashlib
import json
import os
import pwd
import urllib

from django.utils.translation import ugettext_lazy as _

from dojango import forms
from xdmUI.freenas import models, utils


class XDMForm(forms.ModelForm):

    class Meta:
        model = models.XDM
        exclude = (
            'enable',
            )

    def __init__(self, *args, **kwargs):
        self.jail_path = kwargs.pop('jail_path')
        super(XDMForm, self).__init__(*args, **kwargs)

    def save(self, *args, **kwargs):
        obj = super(XDMForm, self).save(*args, **kwargs)

        if obj.enable:
            Popen(["/usr/sbin/sysrc", "xdm_enable=YES"],
                stdout=PIPE,
                stderr=PIPE)
        else:
            Popen(["/usr/sbin/sysrc", "xdm_enable=NO"],
                stdout=PIPE,
                stderr=PIPE)
