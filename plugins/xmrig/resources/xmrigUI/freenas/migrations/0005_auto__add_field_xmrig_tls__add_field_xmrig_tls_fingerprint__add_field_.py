# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'XMRig.tls'
        db.add_column(u'freenas_xmrig', 'tls',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'XMRig.tls_fingerprint'
        db.add_column(u'freenas_xmrig', 'tls_fingerprint',
                      self.gf('django.db.models.fields.CharField')(max_length=120, null=True, blank=True),
                      keep_default=False)

        # Adding field 'XMRig.asm'
        db.add_column(u'freenas_xmrig', 'asm',
                      self.gf('django.db.models.fields.CharField')(default='auto', max_length=120),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'XMRig.tls'
        db.delete_column(u'freenas_xmrig', 'tls')

        # Deleting field 'XMRig.tls_fingerprint'
        db.delete_column(u'freenas_xmrig', 'tls_fingerprint')

        # Deleting field 'XMRig.asm'
        db.delete_column(u'freenas_xmrig', 'asm')


    models = {
        u'freenas.xmrig': {
            'Meta': {'object_name': 'XMRig'},
            'access_token': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'algo': ('django.db.models.fields.CharField', [], {'default': "'cryptonight'", 'max_length': '120'}),
            'asm': ('django.db.models.fields.CharField', [], {'default': "'auto'", 'max_length': '120'}),
            'av': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'cpu_affinity': ('django.db.models.fields.CharField', [], {'max_length': '120', 'null': 'True', 'blank': 'True'}),
            'cpu_priority': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'donate_level': ('django.db.models.fields.IntegerField', [], {'default': '5'}),
            'enable': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ipv6': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'keepalive': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'max_cpu_usage': ('django.db.models.fields.IntegerField', [], {'default': '75'}),
            'nicehash': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'password': ('django.db.models.fields.CharField', [], {'default': "'x'", 'max_length': '500'}),
            'port': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'restricted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'rig_id': ('django.db.models.fields.CharField', [], {'max_length': '120', 'null': 'True', 'blank': 'True'}),
            'safe': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'threads': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'tls': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'tls_fingerprint': ('django.db.models.fields.CharField', [], {'max_length': '120', 'null': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'default': "'donate.v2.xmrig.com:3333'", 'max_length': '500'}),
            'user': ('django.db.models.fields.CharField', [], {'default': "'YOUR_WALLET_ADDRESS'", 'max_length': '500', 'blank': 'True'}),
            'user_agent': ('django.db.models.fields.CharField', [], {'max_length': '120', 'null': 'True', 'blank': 'True'}),
            'variant': ('django.db.models.fields.CharField', [], {'default': "'-1'", 'max_length': '120'}),
            'worker_id': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['freenas']