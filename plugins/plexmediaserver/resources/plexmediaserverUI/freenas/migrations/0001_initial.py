# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'PlexMediaServer'
        db.create_table(u'freenas_plexmediaserver', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('enable', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'freenas', ['PlexMediaServer'])


    def backwards(self, orm):
        # Deleting model 'PlexMediaServer'
        db.delete_table(u'freenas_plexmediaserver')


    models = {
        u'freenas.plexmediaserver': {
            'Meta': {'object_name': 'PlexMediaServer'},
            'enable': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['freenas']