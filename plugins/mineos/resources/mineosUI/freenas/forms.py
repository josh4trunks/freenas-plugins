from subprocess import Popen, PIPE
import hashlib
import json
import os
import pwd
import urllib

from django.utils.translation import ugettext_lazy as _

from dojango import forms
from mineosUI.freenas import models, utils

class MineOSForm(forms.ModelForm):

    class Meta:
        model = models.MineOS
        widgets = {
            'mineos_port': forms.widgets.TextInput(),
        }
        exclude = (
            'enable',
            )

    def __init__(self, *args, **kwargs):
        self.jail_path = kwargs.pop('jail_path')
        super(MineOSForm, self).__init__(*args, **kwargs)

        self.fields['mineos_cert'].widget = \
        self.fields['mineos_key'].widget = forms.widgets.TextInput(attrs={
            'data-dojo-type': 'freeadmin.form.PathSelector',
            'root': self.jail_path,
            'dirsonly': 'false',
            })

        self.fields['mineos_basedir'].widget = forms.widgets.TextInput(attrs={
            'data-dojo-type': 'freeadmin.form.PathSelector',
            'root': self.jail_path,
            'dirsonly': 'true',
            })

    def save(self, *args, **kwargs):
        obj = super(MineOSForm, self).save(*args, **kwargs)

        if obj.enable:
            Popen(["/usr/sbin/sysrc", "mineos_enable=YES"],
                stdout=PIPE,
                stderr=PIPE)
        else:
            Popen(["/usr/sbin/sysrc", "mineos_enable=NO"],
                stdout=PIPE,
                stderr=PIPE)

        settingsfile = os.path.join(utils.mineos_etc_path, "mineos.conf")
        settings = {}

        for field in obj._meta.local_fields:
            if field.attname not in utils.mineos_settings:
                continue
            info = utils.mineos_settings.get(field.attname)
            value = getattr(obj, field.attname)
            _filter = info.get("filter")
            if _filter:
                settings[info.get("field")] = _filter(value)
            else:
                settings[info.get("field")] = value

        with open(settingsfile, 'w') as f:
            f.write("socket_host = '0.0.0.0'\n")
            f.write("socket_port = %d\n" % (obj.mineos_port, ))
            f.write("use_https = %s\n" % (str(obj.mineos_ssl).lower(), ))
            f.write("ssl_certificate = '%s'\n" % (obj.mineos_cert, ))
            f.write("ssl_private_key = '%s'\n" % (obj.mineos_key, ))
            f.write("ssl_cert_chain = ''\n")
            f.write("base_directory = '%s'" % (obj.mineos_basedir, ))
