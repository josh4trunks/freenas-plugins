from subprocess import Popen, PIPE
import hashlib
import json
import os
import pwd
import urllib

from django.utils.translation import ugettext_lazy as _

from dojango import forms
from transmissionUI.freenas import models, utils


class TransmissionForm(forms.ModelForm):

    class Meta:
        model = models.Transmission
        widgets = {
            'rpc_port': forms.widgets.TextInput(),
            'rpc_password': forms.widgets.PasswordInput(),
            'cache_size': forms.widgets.TextInput(),
        }
        exclude = (
            'enable',
            )

    def __init__(self, *args, **kwargs):
        self.jail_path = kwargs.pop('jail_path')
        super(TransmissionForm, self).__init__(*args, **kwargs)

        self.fields['script_torrent_done'].widget = forms.widgets.TextInput(attrs={
            'data-dojo-type': 'freeadmin.form.PathSelector',
            'root': self.jail_path,
            'dirsonly': 'false',
            })

        self.fields['incomplete_dir'].widget = \
        self.fields['watch_dir'].widget = forms.widgets.TextInput(attrs={
            'data-dojo-type': 'freeadmin.form.PathSelector',
            'root': self.jail_path,
            'dirsonly': 'true',
            })

    def clean_rpc_password(self):
        rpc_password = self.cleaned_data.get("rpc_password")
        if not rpc_password:
            return self.instance.rpc_password
        return rpc_password

    def save(self, *args, **kwargs):
        obj = super(TransmissionForm, self).save(*args, **kwargs)

        if obj.enable:
            Popen(["/usr/sbin/sysrc", "transmission_enable=YES"],
                stdout=PIPE,
                stderr=PIPE)
        else:
            Popen(["/usr/sbin/sysrc", "transmission_enable=NO"],
                stdout=PIPE,
                stderr=PIPE)

        settingsfile = os.path.join(utils.transmission_conf_dir, "settings.json")
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
            if field.attname not in utils.transmission_settings:
                continue
            info = utils.transmission_settings.get(field.attname)
            value = getattr(obj, field.attname)
            _filter = info.get("filter")
            if _filter:
                settings[info.get("field")] = _filter(value)
            else:
                settings[info.get("field")] = value

        settings['watch-dir-enabled'] = bool(obj.watch_dir)
        settings['rpc-whitelist-enabled'] = bool(obj.rpc_whitelist)
        settings['incomplete-dir-enabled'] = bool(obj.incomplete_dir)
        settings['script-torrent-done-enabled'] = bool(obj.script_torrent_done)

        with open(settingsfile, 'w') as f:
            f.write(json.dumps(settings, sort_keys=True, indent=4))
