# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Transmission.peer_socket_tos'
        db.delete_column(u'freenas_transmission', 'peer_socket_tos')


    def backwards(self, orm):
        # Adding field 'Transmission.peer_socket_tos'
        db.add_column(u'freenas_transmission', 'peer_socket_tos',
                      self.gf('django.db.models.fields.CharField')(default='default', max_length=120),
                      keep_default=False)


    models = {
        u'freenas.transmission': {
            'Meta': {'object_name': 'Transmission'},
            'cache_size': ('django.db.models.fields.IntegerField', [], {'default': '4'}),
            'enable': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'incomplete_dir': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'permissions': ('django.db.models.fields.IntegerField', [], {'default': '18'}),
            'rpc_auth': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'rpc_auth_required': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'rpc_password': ('django.db.models.fields.CharField', [], {'max_length': '120', 'blank': 'True'}),
            'rpc_port': ('django.db.models.fields.IntegerField', [], {'default': '9091'}),
            'rpc_username': ('django.db.models.fields.CharField', [], {'max_length': '120', 'blank': 'True'}),
            'rpc_whitelist': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'script_torrent_done': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'utp': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'watch_dir': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'})
        }
    }

    complete_apps = ['freenas']