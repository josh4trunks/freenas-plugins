from subprocess import Popen, PIPE
import hashlib
import json
import os
import pwd
import urllib

from django.utils.translation import ugettext_lazy as _

from dojango import forms
from sabnzbdUI.freenas import models, utils


class SABnzbdForm(forms.ModelForm):

    class Meta:
        model = models.SABnzbd
        exclude = (
            'enable',
            )

    def __init__(self, *args, **kwargs):
        self.jail_path = kwargs.pop('jail_path')
        super(SABnzbdForm, self).__init__(*args, **kwargs)

    def save(self, *args, **kwargs):
        obj = super(SABnzbdForm, self).save(*args, **kwargs)

        if obj.enable:
            Popen(["/usr/sbin/sysrc", "sabnzbd_enable=YES"],
                stdout=PIPE,
                stderr=PIPE)
        else:
            Popen(["/usr/sbin/sysrc", "sabnzbd_enable=NO"],
                stdout=PIPE,
                stderr=PIPE)