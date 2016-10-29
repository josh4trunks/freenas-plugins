# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Resilio'
        db.create_table('freenas_resilio', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('enable', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('force_https', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('ssl_certificate', self.gf('django.db.models.fields.CharField')(max_length=500, blank=True)),
            ('ssl_private_key', self.gf('django.db.models.fields.CharField')(max_length=500, blank=True)),
            ('webui_port', self.gf('django.db.models.fields.IntegerField')(default=8888)),
        ))
        db.send_create_signal('freenas', ['Resilio'])


    def backwards(self, orm):
        
        # Deleting model 'Resilio'
        db.delete_table('freenas_resilio')


    models = {
        'freenas.resilio': {
            'Meta': {'object_name': 'Resilio'},
            'enable': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'force_https': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'ssl_certificate': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'ssl_private_key': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'webui_port': ('django.db.models.fields.IntegerField', [], {'default': '8888'}),
        }
    }

    complete_apps = ['freenas']
