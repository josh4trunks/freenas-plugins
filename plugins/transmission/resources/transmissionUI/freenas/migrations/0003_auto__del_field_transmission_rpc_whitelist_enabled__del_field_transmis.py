# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Transmission.rpc_whitelist_enabled'
        db.delete_column(u'freenas_transmission', 'rpc_whitelist_enabled')

        # Deleting field 'Transmission.conf_dir'
        db.delete_column(u'freenas_transmission', 'conf_dir')

        # Deleting field 'Transmission.logfile'
        db.delete_column(u'freenas_transmission', 'logfile')

        # Adding field 'Transmission.incomplete_dir'
        db.add_column(u'freenas_transmission', 'incomplete_dir',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=500, blank=True),
                      keep_default=False)

        # Adding field 'Transmission.blocklist'
        db.add_column(u'freenas_transmission', 'blocklist',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=500, blank=True),
                      keep_default=False)

        # Adding field 'Transmission.permissions'
        db.add_column(u'freenas_transmission', 'permissions',
                      self.gf('django.db.models.fields.IntegerField')(default=18),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Transmission.rpc_whitelist_enabled'
        db.add_column(u'freenas_transmission', 'rpc_whitelist_enabled',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Transmission.conf_dir'
        db.add_column(u'freenas_transmission', 'conf_dir',
                      self.gf('django.db.models.fields.CharField')(default='/usr/pbi/transmission-amd64/etc/transmission/home', max_length=500),
                      keep_default=False)

        # Adding field 'Transmission.logfile'
        db.add_column(u'freenas_transmission', 'logfile',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=500, blank=True),
                      keep_default=False)

        # Deleting field 'Transmission.incomplete_dir'
        db.delete_column(u'freenas_transmission', 'incomplete_dir')

        # Deleting field 'Transmission.blocklist'
        db.delete_column(u'freenas_transmission', 'blocklist')

        # Deleting field 'Transmission.permissions'
        db.delete_column(u'freenas_transmission', 'permissions')


    models = {
        u'freenas.transmission': {
            'Meta': {'object_name': 'Transmission'},
            'blocklist': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'dht': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'download_dir': ('django.db.models.fields.CharField', [], {'default': "'/usr/pbi/transmission-amd64/etc/transmission/home/Downloads'", 'max_length': '500'}),
            'enable': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'encryption': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'global_seedratio': ('django.db.models.fields.DecimalField', [], {'default': '2', 'max_digits': '6', 'decimal_places': '2'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'incomplete_dir': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'lpd': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'peer_port': ('django.db.models.fields.IntegerField', [], {'default': '51413', 'blank': 'True'}),
            'peerlimit_global': ('django.db.models.fields.IntegerField', [], {'default': '240'}),
            'peerlimit_torrent': ('django.db.models.fields.IntegerField', [], {'default': '60'}),
            'permissions': ('django.db.models.fields.IntegerField', [], {'default': '18'}),
            'portmap': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'rpc_auth': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'rpc_auth_required': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'rpc_password': ('django.db.models.fields.CharField', [], {'max_length': '120', 'blank': 'True'}),
            'rpc_port': ('django.db.models.fields.IntegerField', [], {'default': '9091', 'blank': 'True'}),
            'rpc_username': ('django.db.models.fields.CharField', [], {'max_length': '120', 'blank': 'True'}),
            'rpc_whitelist': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'utp': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'watch_dir': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'})
        }
    }

    complete_apps = ['freenas']