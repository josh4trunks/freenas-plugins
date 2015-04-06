from subprocess import Popen, PIPE
import hashlib
import json
import os
import pwd
import urllib
import xml.etree.ElementTree as ET

from django.utils.translation import ugettext_lazy as _

from dojango import forms
from plexmediaserverUI.freenas import models, utils


class PlexMediaServerForm(forms.ModelForm):

    class Meta:
        model = models.PlexMediaServer
        exclude = (
            'enable',
            )

    def __init__(self, *args, **kwargs):
        self.jail_path = kwargs.pop('jail_path')
        super(PlexMediaServerForm, self).__init__(*args, **kwargs)

    def save(self, *args, **kwargs):
        obj = super(PlexMediaServerForm, self).save(*args, **kwargs)

        if obj.enable:
            Popen(["/usr/sbin/sysrc", "plexmediaserver_enable=YES"],
                stdout=PIPE,
                stderr=PIPE)
        else:
            Popen(["/usr/sbin/sysrc", "plexmediaserver_enable=NO"],
                stdout=PIPE,
                stderr=PIPE)

        PLEXMEDIASERVER_PATH = "/var/db/plexdata/Plex Media Server"
        PLEXMEDIASERVER_PREFERENCES_XML = os.path.join(PLEXMEDIASERVER_PATH, "Preferences.xml")
        if os.path.exists(PLEXMEDIASERVER_PREFERENCES_XML):
            tree = ET.parse(PLEXMEDIASERVER_PREFERENCES_XML)
            root = tree.getroot()

            if obj.disable_remote_security:
                root.attrib['disableRemoteSecurity'] = "1"
            else:
                root.attrib['disableRemoteSecurity'] = "0"

            tree.write(PLEXMEDIASERVER_PREFERENCES_XML)
