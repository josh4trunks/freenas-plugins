import hashlib
import json
import os
import pwd
import urllib

from django.utils.translation import ugettext_lazy as _

from dojango import forms
from btsyncUI.freenas import models, utils

class BtSyncForm(forms.ModelForm):

    class Meta:
        model = models.BtSync
        widgets = {
            'webui_port': forms.widgets.TextInput(),
            'config_refresh_interval': forms.widgets.TextInput(),
            'external_port': forms.widgets.TextInput(),
            'folder_rescan_interval': forms.widgets.TextInput(),
            'log_size': forms.widgets.TextInput(),
            'max_file_size_diff_for_patching': forms.widgets.TextInput(),
            'max_file_size_for_versioning': forms.widgets.TextInput(),
            'peer_expiration_days': forms.widgets.TextInput(),
            'sync_max_time_diff': forms.widgets.TextInput(),
            'sync_trash_ttl': forms.widgets.TextInput(),
        }
        exclude = ('enable',)

    def __init__(self, *args, **kwargs):
        self.jail_path = kwargs.pop('jail_path')
        super(BtSyncForm, self).__init__(*args, **kwargs)

    def save(self, *args, **kwargs):
        obj = super(BtSyncForm, self).save(*args, **kwargs)

        rcconf = os.path.join(utils.btsync_etc_path, "rc.conf")
        with open(rcconf, "w") as f:
            if obj.enable:
                f.write('btsync_enable="YES"\n')

        settingsfile = os.path.join(utils.btsync_etc_path, "btsync.conf")
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
            if field.attname not in utils.btsync_settings:
                continue
            info = utils.btsync_settings.get(field.attname)
            value = getattr(obj, field.attname)
            _filter = info.get("filter")
            if _filter:
                settings[info.get("field")] = _filter(value)
            else:
                settings[info.get("field")] = value

        settings['storage_path'] = utils.btsync_datadirectory
	settings['pid_file'] = utils.btsync_pidfile
        settings['webui'] = {}
        settings['webui']['listen'] = "0.0.0.0:" + str(settings.pop("webui_port"))

        with open(settingsfile, 'w') as f:
            f.write(json.dumps(settings, indent=4))

        os.system(os.path.join(utils.btsync_pbi_path, "tweak-rcconf"))
