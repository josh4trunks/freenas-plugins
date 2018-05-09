# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'XMRig.rig_id'
        db.add_column(u'freenas_xmrig', 'rig_id',
                      self.gf('django.db.models.fields.CharField')(max_length=120, null=True, blank=True),
                      keep_default=False)

        # Adding field 'XMRig.user_agent'
        db.add_column(u'freenas_xmrig', 'user_agent',
                      self.gf('django.db.models.fields.CharField')(max_length=120, null=True, blank=True),
                      keep_default=False)

        # Adding field 'XMRig.ipv6'
        db.add_column(u'freenas_xmrig', 'ipv6',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'XMRig.restricted'
        db.add_column(u'freenas_xmrig', 'restricted',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


        # Changing field 'XMRig.variant'
        db.alter_column(u'freenas_xmrig', 'variant', self.gf('django.db.models.fields.CharField')(max_length=120))

    def backwards(self, orm):
        # Deleting field 'XMRig.rig_id'
        db.delete_column(u'freenas_xmrig', 'rig_id')

        # Deleting field 'XMRig.user_agent'
        db.delete_column(u'freenas_xmrig', 'user_agent')

        # Deleting field 'XMRig.ipv6'
        db.delete_column(u'freenas_xmrig', 'ipv6')

        # Deleting field 'XMRig.restricted'
        db.delete_column(u'freenas_xmrig', 'restricted')


        # Changing field 'XMRig.variant'
        db.alter_column(u'freenas_xmrig', 'variant', self.gf('django.db.models.fields.IntegerField')())

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
            'ipv6': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'keepalive': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'max_cpu_usage': ('django.db.models.fields.IntegerField', [], {'default': '75'}),
            'nicehash': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'password': ('django.db.models.fields.CharField', [], {'default': "'x'", 'max_length': '500'}),
            'port': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'restricted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'rig_id': ('django.db.models.fields.CharField', [], {'max_length': '120', 'null': 'True', 'blank': 'True'}),
            'safe': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'threads': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'default': "'proxy.fee.xmrig.com:9999'", 'max_length': '500'}),
            'user': ('django.db.models.fields.CharField', [], {'default': "'YOUR_WALLET'", 'max_length': '500', 'blank': 'True'}),
            'user_agent': ('django.db.models.fields.CharField', [], {'max_length': '120', 'null': 'True', 'blank': 'True'}),
            'variant': ('django.db.models.fields.CharField', [], {'default': "'1'", 'max_length': '120'}),
            'worker_id': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['freenas']
