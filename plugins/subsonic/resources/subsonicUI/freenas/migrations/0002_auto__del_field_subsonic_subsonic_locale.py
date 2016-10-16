# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Subsonic.subsonic_locale'
        db.delete_column(u'freenas_subsonic', 'subsonic_locale')


    def backwards(self, orm):
        # Adding field 'Subsonic.subsonic_locale'
        db.add_column(u'freenas_subsonic', 'subsonic_locale',
                      self.gf('django.db.models.fields.CharField')(default='en_US.UTF-8', max_length=120),
                      keep_default=False)


    models = {
        u'freenas.subsonic': {
            'Meta': {'object_name': 'Subsonic'},
            'enable': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'subsonic_context_path': ('django.db.models.fields.CharField', [], {'default': "'/'", 'max_length': '120'}),
            'subsonic_max_memory': ('django.db.models.fields.IntegerField', [], {'default': '100'}),
            'subsonic_port': ('django.db.models.fields.IntegerField', [], {'default': '4040'}),
            'subsonic_ssl': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'subsonic_ssl_keystore': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'subsonic_ssl_password': ('django.db.models.fields.CharField', [], {'max_length': '120', 'blank': 'True'})
        }
    }

    complete_apps = ['freenas']
