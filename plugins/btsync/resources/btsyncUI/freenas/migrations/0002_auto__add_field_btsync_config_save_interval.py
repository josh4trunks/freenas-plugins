# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'BtSync.config_save_interval'
        db.add_column(u'freenas_btsync', 'config_save_interval',
                      self.gf('django.db.models.fields.IntegerField')(default=600, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'BtSync.config_save_interval'
        db.delete_column(u'freenas_btsync', 'config_save_interval')


    models = {
        u'freenas.btsync': {
            'Meta': {'object_name': 'BtSync'},
            'config_refresh_interval': ('django.db.models.fields.IntegerField', [], {'default': '3600', 'blank': 'True'}),
            'config_save_interval': ('django.db.models.fields.IntegerField', [], {'default': '600', 'blank': 'True'}),
            'disk_low_priority': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'enable': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'external_port': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'folder_rescan_interval': ('django.db.models.fields.IntegerField', [], {'default': '600', 'blank': 'True'}),
            'force_https': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lan_encrypt_data': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'log_size': ('django.db.models.fields.IntegerField', [], {'default': '100', 'blank': 'True'}),
            'max_file_size_diff_for_patching': ('django.db.models.fields.IntegerField', [], {'default': '1000', 'blank': 'True'}),
            'max_file_size_for_versioning': ('django.db.models.fields.IntegerField', [], {'default': '1000', 'blank': 'True'}),
            'peer_expiration_days': ('django.db.models.fields.IntegerField', [], {'default': '7', 'blank': 'True'}),
            'rate_limit_local_peers': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'ssl_certificate': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'ssl_private_key': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'sync_max_time_diff': ('django.db.models.fields.IntegerField', [], {'default': '600', 'blank': 'True'}),
            'sync_trash_ttl': ('django.db.models.fields.IntegerField', [], {'default': '30', 'blank': 'True'}),
            'webui_port': ('django.db.models.fields.IntegerField', [], {'default': '8888', 'blank': 'True'})
        }
    }

    complete_apps = ['freenas']
