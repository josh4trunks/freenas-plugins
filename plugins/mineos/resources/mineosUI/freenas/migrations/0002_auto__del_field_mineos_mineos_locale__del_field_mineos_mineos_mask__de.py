# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'MineOS.mineos_locale'
        db.delete_column(u'freenas_mineos', 'mineos_locale')

        # Deleting field 'MineOS.mineos_mask'
        db.delete_column(u'freenas_mineos', 'mineos_mask')

        # Deleting field 'MineOS.mineos_log'
        db.delete_column(u'freenas_mineos', 'mineos_log')

        # Deleting field 'MineOS.mineos_delay'
        db.delete_column(u'freenas_mineos', 'mineos_delay')


    def backwards(self, orm):
        # Adding field 'MineOS.mineos_locale'
        db.add_column(u'freenas_mineos', 'mineos_locale',
                      self.gf('django.db.models.fields.CharField')(default='en', max_length=120),
                      keep_default=False)

        # Adding field 'MineOS.mineos_mask'
        db.add_column(u'freenas_mineos', 'mineos_mask',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'MineOS.mineos_log'
        db.add_column(u'freenas_mineos', 'mineos_log',
                      self.gf('django.db.models.fields.CharField')(default='/var/log/mineos.log', max_length=500),
                      keep_default=False)

        # Adding field 'MineOS.mineos_delay'
        db.add_column(u'freenas_mineos', 'mineos_delay',
                      self.gf('django.db.models.fields.IntegerField')(default=10),
                      keep_default=False)


    models = {
        u'freenas.mineos': {
            'Meta': {'object_name': 'MineOS'},
            'enable': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mineos_basedir': ('django.db.models.fields.CharField', [], {'default': "'/var/games/minecraft'", 'max_length': '500'}),
            'mineos_cert': ('django.db.models.fields.CharField', [], {'default': "'/etc/ssl/certs/mineos.crt'", 'max_length': '500'}),
            'mineos_key': ('django.db.models.fields.CharField', [], {'default': "'/etc/ssl/certs/mineos.key'", 'max_length': '500'}),
            'mineos_port': ('django.db.models.fields.IntegerField', [], {'default': '8443'}),
            'mineos_ssl': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        }
    }

    complete_apps = ['freenas']