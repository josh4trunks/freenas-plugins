from subprocess import Popen, PIPE
import hashlib
import json
import pwd
import urllib

from django.utils.translation import ugettext_lazy as _

from dojango import forms
from madsonicUI.freenas import models, utils

class MadsonicForm(forms.ModelForm):

    class Meta:
        model = models.Madsonic
        widgets = {
            'madsonic_max_memory': forms.widgets.TextInput(),
            'madsonic_port': forms.widgets.TextInput(),
            'madsonic_ssl_password': forms.widgets.PasswordInput(),
        }
        exclude = (
            'enable',
            )

    def __init__(self, *args, **kwargs):
        self.jail_path = kwargs.pop('jail_path')
        super(MadsonicForm, self).__init__(*args, **kwargs)

        self.fields['madsonic_ssl_keystore'].widget = forms.widgets.TextInput(attrs={
            'data-dojo-type': 'freeadmin.form.PathSelector',
            'root': self.jail_path,
            'dirsonly': 'false',
            })

    def clean_madsonic_ssl_password(self):
        madsonic_ssl_password = self.cleaned_data.get("madsonic_ssl_password")
        if not madsonic_ssl_password:
            return self.instance.madsonic_ssl_password
        return madsonic_ssl_password

    def save(self, *args, **kwargs):
        obj = super(MadsonicForm, self).save(*args, **kwargs)

        if obj.enable:
            Popen(["/usr/sbin/sysrc", "madsonic_enable=YES"],
                stdout=PIPE,
                stderr=PIPE)
        else:
            Popen(["/usr/sbin/sysrc", "madsonic_enable=NO"],
                stdout=PIPE,
                stderr=PIPE)

        settings = {}

        for field in obj._meta.local_fields:
            if field.attname not in utils.madsonic_settings:
                continue
            info = utils.madsonic_settings.get(field.attname)
            value = getattr(obj, field.attname)
            _filter = info.get("filter")
            if _filter:
                settings[info.get("field")] = _filter(value)
            else:
                settings[info.get("field")] = value

        Popen(["/usr/sbin/sysrc", "madsonic_max_memory=%d" % obj.madsonic_max_memory, "madsonic_ssl_keystore=%s" % obj.madsonic_ssl_keystore, "madsonic_ssl_password=%s" % obj.madsonic_ssl_password, "madsonic_port=%d" % obj.madsonic_port, "madsonic_context_path=%s" % obj.madsonic_context_path],
            stdout=PIPE,
            stderr=PIPE)

        if obj.madsonic_ssl:
            Popen(["/usr/sbin/sysrc", "madsonic_ssl=YES"],
                stdout=PIPE,
                stderr=PIPE)
        else:
            Popen(["/usr/sbin/sysrc", "madsonic_ssl=NO"],
                stdout=PIPE,
                stderr=PIPE)
