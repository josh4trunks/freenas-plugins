from subprocess import Popen, PIPE
import hashlib
import json
import os
import pwd
import urllib

from django.utils.translation import ugettext_lazy as _

from dojango import forms
from resilioUI.freenas import models, utils

class ResilioForm(forms.ModelForm):

    class Meta:
        model = models.Resilio
        widgets = {
            'webui_port': forms.widgets.TextInput(),
        }
        exclude = (
            'enable',
            )

    def __init__(self, *args, **kwargs):
        self.jail_path = kwargs.pop('jail_path')
        super(ResilioForm, self).__init__(*args, **kwargs)

        self.fields['ssl_certificate'].widget = \
        self.fields['ssl_private_key'].widget = forms.widgets.TextInput(attrs={
            'data-dojo-type': 'freeadmin.form.PathSelector',
            'root': self.jail_path,
            'dirsonly': 'false',
            })

    def save(self, *args, **kwargs):
        obj = super(ResilioForm, self).save(*args, **kwargs)

        if obj.enable:
            Popen(["/usr/sbin/sysrc", "resilio_enable=YES"],
                stdout=PIPE,
                stderr=PIPE)
        else:
            Popen(["/usr/sbin/sysrc", "resilio_enable=NO"],
                stdout=PIPE,
                stderr=PIPE)

        settingsfile = os.path.join(utils.resilio_etc_path, "resilio.conf")
        if os.path.exists(settingsfile):
            with open(settingsfile, 'r') as f:
                try:
                    settings = json.loads(f.read())
                except:
                    settings = {}
        else:
            try:
                open(settingsfile, 'w').close()
            except OSError:
                #FIXME
                pass
            settings = {}

        for field in obj._meta.local_fields:
            if field.attname not in utils.resilio_settings:
                continue
            info = utils.resilio_settings.get(field.attname)
            value = getattr(obj, field.attname)
            _filter = info.get("filter")
            if _filter:
                settings[info.get("field")] = _filter(value)
            else:
                settings[info.get("field")] = value

        settings['vendor'] = "FreeNAS"
        settings['display_new_version'] = False
        settings['storage_path'] = utils.resilio_datadirectory
        settings['webui'] = {}
        settings['webui']['listen'] = "0.0.0.0:" + str(settings.pop("webui_port"))
        settings['webui']['force_https'] = settings.pop("force_https")
        settings['webui']['ssl_certificate'] = settings.pop("ssl_certificate")
        settings['webui']['ssl_private_key'] = settings.pop("ssl_private_key")

        with open(settingsfile, 'w') as f:
            f.write(json.dumps(settings, indent=4))
