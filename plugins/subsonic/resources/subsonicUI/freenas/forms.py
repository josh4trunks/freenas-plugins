import hashlib
import json
import os
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
        }
        exclude = ('enable',)

    def __init__(self, *args, **kwargs):
        self.jail_path = kwargs.pop('jail_path')
        super(SubsonicForm, self).__init__(*args, **kwargs)

    def save(self, *args, **kwargs):
        obj = super(SubsonicForm, self).save(*args, **kwargs)

        rcconf = os.path.join(utils.subsonic_etc_path, "rc.conf")
        with open(rcconf, "w") as f:
            if obj.enable:
                f.write('subsonic_enable="YES"\n')

        conf_dir = os.path.join(utils.subsonic_etc_path, "subsonic")
        settingsfile = os.path.join(conf_dir, "config.ini")
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

        subsonic_ssl = str(obj.subsonic_ssl).lower()
        with open(settingsfile, 'w') as f:
            f.write('SUBSONIC_MAX_MEMORY="%d"\n' % (obj.subsonic_max_memory, ))
            f.write('SUBSONIC_SSL="%s"\n' % (subsonic_ssl, ))
            f.write('SUBSONIC_PORT="%d"\n' % (obj.subsonic_port, ))
            f.write('SUBSONIC_CONTEXT_PATH="%s"' % (obj.subsonic_context_path, ))

        os.system(os.path.join(utils.subsonic_pbi_path, "tweak-rcconf"))
