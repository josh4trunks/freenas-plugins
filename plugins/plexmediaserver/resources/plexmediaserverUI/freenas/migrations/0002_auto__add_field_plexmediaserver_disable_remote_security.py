# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'PlexMediaServer.disable_remote_security'
        db.add_column(u'freenas_plexmediaserver', 'disable_remote_security',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'PlexMediaServer.disable_remote_security'
        db.delete_column(u'freenas_plexmediaserver', 'disable_remote_security')


    models = {
        u'freenas.plexmediaserver': {
            'Meta': {'object_name': 'PlexMediaServer'},
            'disable_remote_security': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'enable': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['freenas']