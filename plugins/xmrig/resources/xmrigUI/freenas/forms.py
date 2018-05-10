from subprocess import Popen, PIPE
import hashlib
import json
import os
import urllib

from django.utils.translation import ugettext_lazy as _

from dojango import forms
from xmrigUI.freenas import models, utils


class XMRigForm(forms.ModelForm):

    class Meta:
        model = models.XMRig
        widgets = {
            'threads': forms.widgets.TextInput(),
            'max_cpu_usage': forms.widgets.TextInput(),
            'donate_level': forms.widgets.TextInput(),
            'port': forms.widgets.TextInput(),
        }
        exclude = (
            'enable',
            )

    def __init__(self, *args, **kwargs):
        self.jail_path = kwargs.pop('jail_path')
        super(XMRigForm, self).__init__(*args, **kwargs)

    def save(self, *args, **kwargs):
        obj = super(XMRigForm, self).save(*args, **kwargs)

        if obj.enable:
            Popen(["/usr/sbin/sysrc", "xmrig_enable=YES"],
                stdout=PIPE,
                stderr=PIPE)
        else:
            Popen(["/usr/sbin/sysrc", "xmrig_enable=NO"],
                stdout=PIPE,
                stderr=PIPE)

        settingsfile = os.path.join(utils.xmrig_etc_dir, "config.json")
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
            if field.attname not in utils.xmrig_settings:
                continue
            info = utils.xmrig_settings.get(field.attname)
            value = getattr(obj, field.attname)
            _filter = info.get("filter")
            if _filter:
                settings[info.get("field")] = _filter(value)
            else:
                settings[info.get("field")] = value

        if not obj.rig_id:
            settings['rig-id'] = None
        settings['pools'] = []
        settings['pools'].append({'url':settings.pop("url"), 'user':settings.pop("user"), 'pass':settings.pop("pass"), 'rig-id':settings.pop("rig-id"), 'nicehash':settings.pop("nicehash"), 'keepalive':settings.pop("keepalive"), 'variant':settings.pop("variant")})
        settings['api'] = {}
        settings['api']['port'] = settings.pop("port")
        if obj.access_token:
            settings['api']['access-token'] = obj.access_token
        settings.pop("access-token")
        if obj.worker_id:
            settings['api']['worker-id'] = obj.worker_id
        settings.pop("worker-id")
        settings['api']['ipv6'] = settings.pop("ipv6")
        settings['api']['restricted'] = settings.pop("restricted")
        if not obj.user_agent:
            settings.pop("user-agent")

        with open(settingsfile, 'w') as f:
            f.write(json.dumps(settings, sort_keys=True, indent=4))
