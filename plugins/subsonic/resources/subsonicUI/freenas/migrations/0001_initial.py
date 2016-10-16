# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Subsonic'
        db.create_table('freenas_subsonic', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('enable', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('subsonic_max_memory', self.gf('django.db.models.fields.IntegerField')(default=100)),
            ('subsonic_ssl', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('subsonic_ssl_keystore', self.gf('django.db.models.fields.CharField')(max_length=500, blank=True)),
            ('subsonic_ssl_password', self.gf('django.db.models.fields.CharField')(max_length=120, blank=True)),
            ('subsonic_port', self.gf('django.db.models.fields.IntegerField')(default=4040)),
            ('subsonic_context_path', self.gf('django.db.models.fields.CharField')(default='/', max_length=120)),
            ('subsonic_locale', self.gf('django.db.models.fields.CharField')(default='en_US.UTF-8', max_length=120)),
        ))
        db.send_create_signal('freenas', ['Subsonic'])


    def backwards(self, orm):
        
        # Deleting model 'Subsonic'
        db.delete_table('freenas_subsonic')


    models = {
        'freenas.subsonic': {
            'Meta': {'object_name': 'Subsonic'},
            'enable': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'subsonic_max_memory': ('django.db.models.fields.IntegerField', [], {'default': '100'}),
            'subsonic_ssl': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'subsonic_ssl_keystore': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'subsonic_ssl_password': ('django.db.models.fields.CharField', [], {'max_length': '120', 'blank': 'True'}),
            'subsonic_port': ('django.db.models.fields.IntegerField', [], {'default': '4040'}),
            'subsonic_context_path': ('django.db.models.fields.CharField', [], {'default': "'/'", 'max_length': '120'}),
            'subsonic_locale': ('django.db.models.fields.CharField', [], {'default': "'en_US.UTF-8'", 'max_length': '120'}),
        }
    }

    complete_apps = ['freenas']
