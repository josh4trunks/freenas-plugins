# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'XMRig'
        db.create_table(u'freenas_xmrig', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('enable', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('algo', self.gf('django.db.models.fields.CharField')(default='cryptonight', max_length=120)),
            ('cpu_affinity', self.gf('django.db.models.fields.CharField')(max_length=120, blank=True)),
            ('donate_level', self.gf('django.db.models.fields.IntegerField')(default=5)),
            ('url', self.gf('django.db.models.fields.CharField')(default='pool.minemonero.pro:5555', max_length=500)),
            ('user', self.gf('django.db.models.fields.CharField')(max_length=500, blank=True)),
            ('password', self.gf('django.db.models.fields.CharField')(default='x', max_length=500)),
            ('keepalive', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('nicehash', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('port', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'freenas', ['XMRig'])


    def backwards(self, orm):
        # Deleting model 'XMRig'
        db.delete_table(u'freenas_xmrig')


    models = {
        u'freenas.xmrig': {
            'Meta': {'object_name': 'XMRig'},
            'algo': ('django.db.models.fields.CharField', [], {'default': "'cryptonight'", 'max_length': '120'}),
            'cpu_affinity': ('django.db.models.fields.CharField', [], {'max_length': '120', 'blank': 'True'}),
            'donate_level': ('django.db.models.fields.IntegerField', [], {'default': '5'}),
            'enable': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keepalive': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'nicehash': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'password': ('django.db.models.fields.CharField', [], {'default': "'x'", 'max_length': '500'}),
            'port': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'url': ('django.db.models.fields.CharField', [], {'default': "'pool.minemonero.pro:5555'", 'max_length': '500'}),
            'user': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'})
        }
    }

    complete_apps = ['freenas']
