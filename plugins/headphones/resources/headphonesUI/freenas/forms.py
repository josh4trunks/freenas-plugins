from subprocess import Popen, PIPE
import hashlib
import json
import pwd
import urllib

from django.utils.translation import ugettext_lazy as _

from dojango import forms
from headphonesUI.freenas import models, utils


class HeadphonesForm(forms.ModelForm):

    class Meta:
        model = models.Headphones
        exclude = (
            'enable',
            )

    def __init__(self, *args, **kwargs):
        self.jail_path = kwargs.pop('jail_path')
        super(HeadphonesForm, self).__init__(*args, **kwargs)

    def save(self, *args, **kwargs):
        obj = super(HeadphonesForm, self).save(*args, **kwargs)

        if obj.enable:
            Popen(["/usr/sbin/sysrc", "headphones_enable=YES"],
                stdout=PIPE,
                stderr=PIPE)
        else:
            Popen(["/usr/sbin/sysrc", "headphones_enable=NO"],
                stdout=PIPE,
                stderr=PIPE)