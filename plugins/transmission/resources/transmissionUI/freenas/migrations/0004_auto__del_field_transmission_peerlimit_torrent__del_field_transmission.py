# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Transmission.peerlimit_torrent'
        db.delete_column(u'freenas_transmission', 'peerlimit_torrent')

        # Deleting field 'Transmission.encryption'
        db.delete_column(u'freenas_transmission', 'encryption')

        # Deleting field 'Transmission.dht'
        db.delete_column(u'freenas_transmission', 'dht')

        # Deleting field 'Transmission.global_seedratio'
        db.delete_column(u'freenas_transmission', 'global_seedratio')

        # Deleting field 'Transmission.download_dir'
        db.delete_column(u'freenas_transmission', 'download_dir')

        # Deleting field 'Transmission.portmap'
        db.delete_column(u'freenas_transmission', 'portmap')

        # Deleting field 'Transmission.peer_port'
        db.delete_column(u'freenas_transmission', 'peer_port')

        # Deleting field 'Transmission.blocklist'
        db.delete_column(u'freenas_transmission', 'blocklist')

        # Deleting field 'Transmission.peerlimit_global'
        db.delete_column(u'freenas_transmission', 'peerlimit_global')

        # Deleting field 'Transmission.lpd'
        db.delete_column(u'freenas_transmission', 'lpd')

        # Adding field 'Transmission.script_torrent_done'
        db.add_column(u'freenas_transmission', 'script_torrent_done',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=500, blank=True),
                      keep_default=False)

        # Adding field 'Transmission.cache_size'
        db.add_column(u'freenas_transmission', 'cache_size',
                      self.gf('django.db.models.fields.IntegerField')(default=4),
                      keep_default=False)

        # Adding field 'Transmission.peer_socket_tos'
        db.add_column(u'freenas_transmission', 'peer_socket_tos',
                      self.gf('django.db.models.fields.CharField')(default='default', max_length=120),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Transmission.peerlimit_torrent'
        db.add_column(u'freenas_transmission', 'peerlimit_torrent',
                      self.gf('django.db.models.fields.IntegerField')(default=60),
                      keep_default=False)

        # Adding field 'Transmission.encryption'
        db.add_column(u'freenas_transmission', 'encryption',
                      self.gf('django.db.models.fields.IntegerField')(default=1),
                      keep_default=False)

        # Adding field 'Transmission.dht'
        db.add_column(u'freenas_transmission', 'dht',
                      self.gf('django.db.models.fields.BooleanField')(default=True),
                      keep_default=False)

        # Adding field 'Transmission.global_seedratio'
        db.add_column(u'freenas_transmission', 'global_seedratio',
                      self.gf('django.db.models.fields.DecimalField')(default=2, max_digits=6, decimal_places=2),
                      keep_default=False)

        # Adding field 'Transmission.download_dir'
        db.add_column(u'freenas_transmission', 'download_dir',
                      self.gf('django.db.models.fields.CharField')(default='/usr/pbi/transmission-amd64/etc/transmission/home/Downloads', max_length=500),
                      keep_default=False)

        # Adding field 'Transmission.portmap'
        db.add_column(u'freenas_transmission', 'portmap',
                      self.gf('django.db.models.fields.BooleanField')(default=True),
                      keep_default=False)

        # Adding field 'Transmission.peer_port'
        db.add_column(u'freenas_transmission', 'peer_port',
                      self.gf('django.db.models.fields.IntegerField')(default=51413, blank=True),
                      keep_default=False)

        # Adding field 'Transmission.blocklist'
        db.add_column(u'freenas_transmission', 'blocklist',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=500, blank=True),
                      keep_default=False)

        # Adding field 'Transmission.peerlimit_global'
        db.add_column(u'freenas_transmission', 'peerlimit_global',
                      self.gf('django.db.models.fields.IntegerField')(default=240),
                      keep_default=False)

        # Adding field 'Transmission.lpd'
        db.add_column(u'freenas_transmission', 'lpd',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Deleting field 'Transmission.script_torrent_done'
        db.delete_column(u'freenas_transmission', 'script_torrent_done')

        # Deleting field 'Transmission.cache_size'
        db.delete_column(u'freenas_transmission', 'cache_size')

        # Deleting field 'Transmission.peer_socket_tos'
        db.delete_column(u'freenas_transmission', 'peer_socket_tos')


    models = {
        u'freenas.transmission': {
            'Meta': {'object_name': 'Transmission'},
            'cache_size': ('django.db.models.fields.IntegerField', [], {'default': '4'}),
            'enable': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'incomplete_dir': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'peer_socket_tos': ('django.db.models.fields.CharField', [], {'default': "'default'", 'max_length': '120'}),
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