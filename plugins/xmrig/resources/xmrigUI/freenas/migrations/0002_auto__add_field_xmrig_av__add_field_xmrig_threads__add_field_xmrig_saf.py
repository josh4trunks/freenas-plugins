# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'XMRig.av'
        db.add_column(u'freenas_xmrig', 'av',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'XMRig.threads'
        db.add_column(u'freenas_xmrig', 'threads',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'XMRig.safe'
        db.add_column(u'freenas_xmrig', 'safe',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'XMRig.max_cpu_usage'
        db.add_column(u'freenas_xmrig', 'max_cpu_usage',
                      self.gf('django.db.models.fields.IntegerField')(default=75),
                      keep_default=False)

        # Adding field 'XMRig.cpu_priority'
        db.add_column(u'freenas_xmrig', 'cpu_priority',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'XMRig.access_token'
        db.add_column(u'freenas_xmrig', 'access_token',
                      self.gf('django.db.models.fields.CharField')(max_length=500, null=True, blank=True),
                      keep_default=False)

        # Adding field 'XMRig.worker_id'
        db.add_column(u'freenas_xmrig', 'worker_id',
                      self.gf('django.db.models.fields.CharField')(max_length=500, null=True, blank=True),
                      keep_default=False)


        # Changing field 'XMRig.cpu_affinity'
        db.alter_column(u'freenas_xmrig', 'cpu_affinity', self.gf('django.db.models.fields.CharField')(max_length=120, null=True))

    def backwards(self, orm):
        # Deleting field 'XMRig.av'
        db.delete_column(u'freenas_xmrig', 'av')

        # Deleting field 'XMRig.threads'
        db.delete_column(u'freenas_xmrig', 'threads')

        # Deleting field 'XMRig.safe'
        db.delete_column(u'freenas_xmrig', 'safe')

        # Deleting field 'XMRig.max_cpu_usage'
        db.delete_column(u'freenas_xmrig', 'max_cpu_usage')

        # Deleting field 'XMRig.cpu_priority'
        db.delete_column(u'freenas_xmrig', 'cpu_priority')

        # Deleting field 'XMRig.access_token'
        db.delete_column(u'freenas_xmrig', 'access_token')

        # Deleting field 'XMRig.worker_id'
        db.delete_column(u'freenas_xmrig', 'worker_id')


        # Changing field 'XMRig.cpu_affinity'
        db.alter_column(u'freenas_xmrig', 'cpu_affinity', self.gf('django.db.models.fields.CharField')(default='', max_length=120))

    models = {
        u'freenas.xmrig': {
            'Meta': {'object_name': 'XMRig'},
            'access_token': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'algo': ('django.db.models.fields.CharField', [], {'default': "'cryptonight'", 'max_length': '120'}),
            'av': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'cpu_affinity': ('django.db.models.fields.CharField', [], {'max_length': '120', 'null': 'True', 'blank': 'True'}),
            'cpu_priority': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'donate_level': ('django.db.models.fields.IntegerField', [], {'default': '5'}),
            'enable': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keepalive': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'max_cpu_usage': ('django.db.models.fields.IntegerField', [], {'default': '75'}),
            'nicehash': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'password': ('django.db.models.fields.CharField', [], {'default': "'x'", 'max_length': '500'}),
            'port': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'safe': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'threads': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'default': "'pool.minemonero.pro:5555'", 'max_length': '500'}),
            'user': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'worker_id': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['freenas']