# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'MineOS'
        db.create_table('freenas_mineos', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('enable', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('mineos_ssl', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('mineos_cert', self.gf('django.db.models.fields.CharField')(default='/etc/ssl/certs/mineos.crt', max_length=500)),
            ('mineos_key', self.gf('django.db.models.fields.CharField')(default='/etc/ssl/certs/mineos.key', max_length=500)),
            ('mineos_port', self.gf('django.db.models.fields.IntegerField')(default=8080)),
            ('mineos_mask', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('mineos_locale', self.gf('django.db.models.fields.CharField')(default='en', max_length=120)),
            ('mineos_delay', self.gf('django.db.models.fields.IntegerField')(default=10)),
            ('mineos_basedir', self.gf('django.db.models.fields.CharField')(default='/var/games/minecraft', max_length=500)),
            ('mineos_log', self.gf('django.db.models.fields.CharField')(default='/var/log/mineos.log', max_length=500)),
        ))
        db.send_create_signal('freenas', ['MineOS'])


    def backwards(self, orm):
        
        # Deleting model 'MineOS'
        db.delete_table('freenas_mineos')


    models = {
        'freenas.mineos': {
            'Meta': {'object_name': 'MineOS'},
            'enable': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mineos_ssl': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'mineos_cert': ('django.db.models.fields.CharField', [], {'default': '/etc/ssl/certs/mineos.crt', 'max_length': '500'}),
            'mineos_key': ('django.db.models.fields.CharField', [], {'default': '/etc/ssl/certs/mineos.key', 'max_length': '500'}),
            'mineos_port': ('django.db.models.fields.IntegerField', [], {'default': '8080'}),
            'mineos_mask': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'mineos_locale': ('django.db.models.fields.CharField', [], {'default': "'en'", 'max_length': '120'}),
            'mineos_delay': ('django.db.models.fields.IntegerField', [], {'default': '10'}),
            'mineos_basedir': ('django.db.models.fields.CharField', [], {'default': '/var/games/minecraft', 'max_length': '500'}),
            'mineos_log': ('django.db.models.fields.CharField', [], {'default': '/var/log/mineos.log', 'max_length': '500'}),
        }
    }

    complete_apps = ['freenas']
