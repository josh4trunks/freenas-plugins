# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'BtSync.config_refresh_interval'
        db.delete_column(u'freenas_btsync', 'config_refresh_interval')

        # Deleting field 'BtSync.lan_encrypt_data'
        db.delete_column(u'freenas_btsync', 'lan_encrypt_data')

        # Deleting field 'BtSync.sync_trash_ttl'
        db.delete_column(u'freenas_btsync', 'sync_trash_ttl')

        # Deleting field 'BtSync.log_size'
        db.delete_column(u'freenas_btsync', 'log_size')

        # Deleting field 'BtSync.rate_limit_local_peers'
        db.delete_column(u'freenas_btsync', 'rate_limit_local_peers')

        # Deleting field 'BtSync.folder_rescan_interval'
        db.delete_column(u'freenas_btsync', 'folder_rescan_interval')

        # Deleting field 'BtSync.max_file_size_for_versioning'
        db.delete_column(u'freenas_btsync', 'max_file_size_for_versioning')

        # Deleting field 'BtSync.peer_expiration_days'
        db.delete_column(u'freenas_btsync', 'peer_expiration_days')

        # Deleting field 'BtSync.sync_max_time_diff'
        db.delete_column(u'freenas_btsync', 'sync_max_time_diff')

        # Deleting field 'BtSync.max_file_size_diff_for_patching'
        db.delete_column(u'freenas_btsync', 'max_file_size_diff_for_patching')

        # Deleting field 'BtSync.config_save_interval'
        db.delete_column(u'freenas_btsync', 'config_save_interval')

        # Deleting field 'BtSync.external_port'
        db.delete_column(u'freenas_btsync', 'external_port')

        # Deleting field 'BtSync.disk_low_priority'
        db.delete_column(u'freenas_btsync', 'disk_low_priority')


    def backwards(self, orm):
        # Adding field 'BtSync.config_refresh_interval'
        db.add_column(u'freenas_btsync', 'config_refresh_interval',
                      self.gf('django.db.models.fields.IntegerField')(default=3600, blank=True),
                      keep_default=False)

        # Adding field 'BtSync.lan_encrypt_data'
        db.add_column(u'freenas_btsync', 'lan_encrypt_data',
                      self.gf('django.db.models.fields.BooleanField')(default=True),
                      keep_default=False)

        # Adding field 'BtSync.sync_trash_ttl'
        db.add_column(u'freenas_btsync', 'sync_trash_ttl',
                      self.gf('django.db.models.fields.IntegerField')(default=30, blank=True),
                      keep_default=False)

        # Adding field 'BtSync.log_size'
        db.add_column(u'freenas_btsync', 'log_size',
                      self.gf('django.db.models.fields.IntegerField')(default=100, blank=True),
                      keep_default=False)

        # Adding field 'BtSync.rate_limit_local_peers'
        db.add_column(u'freenas_btsync', 'rate_limit_local_peers',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'BtSync.folder_rescan_interval'
        db.add_column(u'freenas_btsync', 'folder_rescan_interval',
                      self.gf('django.db.models.fields.IntegerField')(default=600, blank=True),
                      keep_default=False)

        # Adding field 'BtSync.max_file_size_for_versioning'
        db.add_column(u'freenas_btsync', 'max_file_size_for_versioning',
                      self.gf('django.db.models.fields.IntegerField')(default=1000, blank=True),
                      keep_default=False)

        # Adding field 'BtSync.peer_expiration_days'
        db.add_column(u'freenas_btsync', 'peer_expiration_days',
                      self.gf('django.db.models.fields.IntegerField')(default=7, blank=True),
                      keep_default=False)

        # Adding field 'BtSync.sync_max_time_diff'
        db.add_column(u'freenas_btsync', 'sync_max_time_diff',
                      self.gf('django.db.models.fields.IntegerField')(default=600, blank=True),
                      keep_default=False)

        # Adding field 'BtSync.max_file_size_diff_for_patching'
        db.add_column(u'freenas_btsync', 'max_file_size_diff_for_patching',
                      self.gf('django.db.models.fields.IntegerField')(default=1000, blank=True),
                      keep_default=False)

        # Adding field 'BtSync.config_save_interval'
        db.add_column(u'freenas_btsync', 'config_save_interval',
                      self.gf('django.db.models.fields.IntegerField')(default=600, blank=True),
                      keep_default=False)

        # Adding field 'BtSync.external_port'
        db.add_column(u'freenas_btsync', 'external_port',
                      self.gf('django.db.models.fields.IntegerField')(default=0, blank=True),
                      keep_default=False)

        # Adding field 'BtSync.disk_low_priority'
        db.add_column(u'freenas_btsync', 'disk_low_priority',
                      self.gf('django.db.models.fields.BooleanField')(default=True),
                      keep_default=False)


    models = {
        u'freenas.btsync': {
            'Meta': {'object_name': 'BtSync'},
            'enable': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'force_https': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ssl_certificate': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'ssl_private_key': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'webui_port': ('django.db.models.fields.IntegerField', [], {'default': '8888'})
        }
    }

    complete_apps = ['freenas']