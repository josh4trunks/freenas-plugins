# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'BtSync.profiler_enabled'
        db.add_column(u'freenas_btsync', 'profiler_enabled',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'BtSync.send_statistics'
        db.add_column(u'freenas_btsync', 'send_statistics',
                      self.gf('django.db.models.fields.BooleanField')(default=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'BtSync.profiler_enabled'
        db.delete_column(u'freenas_btsync', 'profiler_enabled')

        # Deleting field 'BtSync.send_statistics'
        db.delete_column(u'freenas_btsync', 'send_statistics')


    models = {
        u'freenas.btsync': {
            'Meta': {'object_name': 'BtSync'},
            'config_refresh_interval': ('django.db.models.fields.IntegerField', [], {'default': '3600'}),
            'config_save_interval': ('django.db.models.fields.IntegerField', [], {'default': '600'}),
            'disk_low_priority': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'enable': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'external_port': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'folder_rescan_interval': ('django.db.models.fields.IntegerField', [], {'default': '600'}),
            'force_https': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lan_encrypt_data': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'log_size': ('django.db.models.fields.IntegerField', [], {'default': '100'}),
            'max_file_size_diff_for_patching': ('django.db.models.fields.IntegerField', [], {'default': '1000'}),
            'max_file_size_for_versioning': ('django.db.models.fields.IntegerField', [], {'default': '1000'}),
            'peer_expiration_days': ('django.db.models.fields.IntegerField', [], {'default': '7'}),
            'profiler_enabled': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'rate_limit_local_peers': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'send_statistics': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'ssl_certificate': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'ssl_private_key': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'sync_max_time_diff': ('django.db.models.fields.IntegerField', [], {'default': '600'}),
            'sync_trash_ttl': ('django.db.models.fields.IntegerField', [], {'default': '30'}),
            'webui_port': ('django.db.models.fields.IntegerField', [], {'default': '8888'})
        }
    }

    complete_apps = ['freenas']