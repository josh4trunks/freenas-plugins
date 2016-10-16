from subprocess import Popen, PIPE
import hashlib
import json
import pwd
import urllib

from django.utils.translation import ugettext_lazy as _

from dojango import forms
from subsonicUI.freenas import models, utils

class SubsonicForm(forms.ModelForm):

    class Meta:
        model = models.Subsonic
        widgets = {
            'subsonic_max_memory': forms.widgets.TextInput(),
            'subsonic_port': forms.widgets.TextInput(),
            'subsonic_ssl_password': forms.widgets.PasswordInput(),
        }
        exclude = (
            'enable',
            )

    def __init__(self, *args, **kwargs):
        self.jail_path = kwargs.pop('jail_path')
        super(SubsonicForm, self).__init__(*args, **kwargs)

        self.fields['subsonic_ssl_keystore'].widget = forms.widgets.TextInput(attrs={
            'data-dojo-type': 'freeadmin.form.PathSelector',
            'root': self.jail_path,
            'dirsonly': 'false',
            })

    def clean_subsonic_ssl_password(self):
        subsonic_ssl_password = self.cleaned_data.get("subsonic_ssl_password")
        if not subsonic_ssl_password:
            return self.instance.subsonic_ssl_password
        return subsonic_ssl_password

    def save(self, *args, **kwargs):
        obj = super(SubsonicForm, self).save(*args, **kwargs)

        if obj.enable:
            Popen(["/usr/sbin/sysrc", "subsonic_enable=YES"],
                stdout=PIPE,
                stderr=PIPE)
        else:
            Popen(["/usr/sbin/sysrc", "subsonic_enable=NO"],
                stdout=PIPE,
                stderr=PIPE)

        settings = {}

        for field in obj._meta.local_fields:
            if field.attname not in utils.subsonic_settings:
                continue
            info = utils.subsonic_settings.get(field.attname)
            value = getattr(obj, field.attname)
            _filter = info.get("filter")
            if _filter:
                settings[info.get("field")] = _filter(value)
            else:
                settings[info.get("field")] = value

        Popen(["/usr/sbin/sysrc", "subsonic_max_memory=%d" % obj.subsonic_max_memory, "subsonic_ssl_keystore=%s" % obj.subsonic_ssl_keystore, "subsonic_ssl_password=%s" % obj.subsonic_ssl_password, "subsonic_port=%d" % obj.subsonic_port, "subsonic_context_path=%s" % obj.subsonic_context_path],
            stdout=PIPE,
            stderr=PIPE)

        if obj.subsonic_ssl:
            Popen(["/usr/sbin/sysrc", "subsonic_ssl=YES"],
                stdout=PIPE,
                stderr=PIPE)
        else:
            Popen(["/usr/sbin/sysrc", "subsonic_ssl=NO"],
                stdout=PIPE,
                stderr=PIPE)
