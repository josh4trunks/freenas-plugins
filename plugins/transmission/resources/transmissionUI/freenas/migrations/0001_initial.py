# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Transmission'
        db.create_table('freenas_transmission', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('enable', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('watch_dir', self.gf('django.db.models.fields.CharField')(max_length=500, blank=True)),
            ('download_dir', self.gf('django.db.models.fields.CharField')(default='/usr/pbi/transmission-amd64/etc/transmission/home/Downloads', max_length=500)),
            ('incomplete_dir', self.gf('django.db.models.fields.CharField')(max_length=500, blank=True)),
            ('rpc_port', self.gf('django.db.models.fields.IntegerField')(default=9091, blank=True)),
            ('rpc_auth', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('rpc_auth_required', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('rpc_username', self.gf('django.db.models.fields.CharField')(max_length=120, blank=True)),
            ('rpc_password', self.gf('django.db.models.fields.CharField')(max_length=120, blank=True)),
            ('rpc_whitelist', self.gf('django.db.models.fields.CharField')(max_length=500, blank=True)),
            ('dht', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('lpd', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('utp', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('peer_port', self.gf('django.db.models.fields.IntegerField')(default=51413, blank=True)),
            ('portmap', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('peerlimit_global', self.gf('django.db.models.fields.IntegerField')(default=240)),
            ('peerlimit_torrent', self.gf('django.db.models.fields.IntegerField')(default=60)),
            ('encryption', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('blocklist', self.gf('django.db.models.fields.CharField')(max_length=500, blank=True)),
            ('global_seedratio', self.gf('django.db.models.fields.IntegerField')(default=2)),
            ('permissions', self.gf('django.db.models.fields.IntegerField')(default=18)),
        ))
        db.send_create_signal('freenas', ['Transmission'])


    def backwards(self, orm):
        
        # Deleting model 'Transmission'
        db.delete_table('freenas_transmission')


    models = {
        'freenas.transmission': {
            'Meta': {'object_name': 'Transmission'},
            'dht': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'download_dir': ('django.db.models.fields.CharField', [], {'default': "'/usr/pbi/transmission-amd64/etc/transmission/home/Downloads'", 'max_length': '500'}),
            'incomplete_dir': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'enable': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'blocklist': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'encryption': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'permissions': ('django.db.models.fields.IntegerField', [], {'default': '18'}),
            'global_seedratio': ('django.db.models.fields.IntegerField', [], {'default': '2'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lpd': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'peer_port': ('django.db.models.fields.IntegerField', [], {'default': '51413', 'blank': 'True'}),
            'peerlimit_global': ('django.db.models.fields.IntegerField', [], {'default': '240'}),
            'peerlimit_torrent': ('django.db.models.fields.IntegerField', [], {'default': '60'}),
            'portmap': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'rpc_auth': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'rpc_auth_required': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'rpc_password': ('django.db.models.fields.CharField', [], {'max_length': '120', 'blank': 'True'}),
            'rpc_port': ('django.db.models.fields.IntegerField', [], {'default': '9091', 'blank': 'True'}),
            'rpc_username': ('django.db.models.fields.CharField', [], {'max_length': '120', 'blank': 'True'}),
            'rpc_whitelist': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'utp': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'watch_dir': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'})
        }
    }

    complete_apps = ['freenas']
