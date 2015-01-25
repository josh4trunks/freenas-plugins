from subprocess import Popen, PIPE
import hashlib
import json
import pwd
import urllib

from django.utils.translation import ugettext_lazy as _

from dojango import forms
from mediabrowserUI.freenas import models, utils


class MediaBrowserForm(forms.ModelForm):

    class Meta:
        model = models.MediaBrowser
        exclude = (
            'enable',
            )

    def __init__(self, *args, **kwargs):
        self.jail_path = kwargs.pop('jail_path')
        super(MediaBrowserForm, self).__init__(*args, **kwargs)

    def save(self, *args, **kwargs):
        obj = super(MediaBrowserForm, self).save(*args, **kwargs)

        if obj.enable:
            Popen(["/usr/sbin/sysrc", "mediabrowser_enable=YES"],
                stdout=PIPE,
                stderr=PIPE)
        else:
            Popen(["/usr/sbin/sysrc", "mediabrowser_enable=NO"],
                stdout=PIPE,
                stderr=PIPE)