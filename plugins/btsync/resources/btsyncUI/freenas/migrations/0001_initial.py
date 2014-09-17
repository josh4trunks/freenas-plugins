# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'BtSync'
        db.create_table('freenas_btsync', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('enable', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('webui_port', self.gf('django.db.models.fields.IntegerField')(default=8888)),
            ('config_refresh_interval', self.gf('django.db.models.fields.IntegerField')(default=3600)),
            ('disk_low_priority', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('external_port', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('folder_rescan_interval', self.gf('django.db.models.fields.IntegerField')(default=600)),
            ('lan_encrypt_data', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('log_size', self.gf('django.db.models.fields.IntegerField')(default=10)),
            ('max_file_size_diff_for_patching', self.gf('django.db.models.fields.IntegerField')(default=1000)),
            ('max_file_size_for_versioning', self.gf('django.db.models.fields.IntegerField')(default=1000)),
            ('peer_expiration_days', self.gf('django.db.models.fields.IntegerField')(default=7)),
            ('rate_limit_local_peers', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('sync_max_time_diff', self.gf('django.db.models.fields.IntegerField')(default=600)),
            ('sync_trash_ttl', self.gf('django.db.models.fields.IntegerField')(default=30)),
        ))
        db.send_create_signal('freenas', ['BtSync'])


    def backwards(self, orm):
        
        # Deleting model 'BtSync'
        db.delete_table('freenas_btsync')


    models = {
        'freenas.btsync': {
            'Meta': {'object_name': 'BtSync'},
            'enable': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'webui_port': ('django.db.models.fields.IntegerField', [], {'default': '8888'}),
            'config_refresh_interval': ('django.db.models.fields.IntegerField', [], {'default': '3600'}),
            'disk_low_priority': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'external_port': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'folder_rescan_interval': ('django.db.models.fields.IntegerField', [], {'default': '600'}),
            'lan_encrypt_data': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'log_size': ('django.db.models.fields.IntegerField', [], {'default': '10'}),
            'max_file_size_diff_for_patching': ('django.db.models.fields.IntegerField', [], {'default': '1000'}),
            'max_file_size_for_versioning': ('django.db.models.fields.IntegerField', [], {'default': '1000'}),
            'peer_expiration_days': ('django.db.models.fields.IntegerField', [], {'default': '7'}),
            'rate_limit_local_peers': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'sync_max_time_diff': ('django.db.models.fields.IntegerField', [], {'default': '600'}),
            'sync_trash_ttl': ('django.db.models.fields.IntegerField', [], {'default': '30'}),
        }
    }

    complete_apps = ['freenas']
