from subprocess import Popen, PIPE
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
        exclude = (
            'enable',
            )

    def __init__(self, *args, **kwargs):
        self.jail_path = kwargs.pop('jail_path')
        super(MylarForm, self).__init__(*args, **kwargs)

    def save(self, *args, **kwargs):
        obj = super(MylarForm, self).save(*args, **kwargs)

        if obj.enable:
            Popen(["/usr/sbin/sysrc", "mylar_enable=YES"],
                stdout=PIPE,
                stderr=PIPE)
        else:
            Popen(["/usr/sbin/sysrc", "mylar_enable=NO"],
                stdout=PIPE,
                stderr=PIPE)