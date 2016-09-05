#!/bin/sh
#########################################

plexmediaserver_pbi_path=/usr/pbi/plexmediaserver-$(uname -m)

${plexmediaserver_pbi_path}/bin/python2.7 ${plexmediaserver_pbi_path}/plexmediaserverUI/manage.py syncdb --migrate --noinput

# Temporary
sysrc 'plexmediaserver_support_path=/var/db/plexdata'
chmod 555 "${plexmediaserver_pbi_path}/share/plexmediaserver/Plex DLNA Server" \
	"${plexmediaserver_pbi_path}/share/plexmediaserver/Plex Media Scanner" \
	"${plexmediaserver_pbi_path}/share/plexmediaserver/Plex Media Server" \
	"${plexmediaserver_pbi_path}/share/plexmediaserver/Plex Relay" \
	"${plexmediaserver_pbi_path}/share/plexmediaserver/Plex Script Host" \
	"${plexmediaserver_pbi_path}/share/plexmediaserver/Plex Transcoder"
chmod 644 ${plexmediaserver_pbi_path}/share/plexmediaserver/Resources/com.plexapp.plugins.library.db	
