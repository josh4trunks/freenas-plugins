#!/bin/sh
#########################################

plexmediaserver_resources="/usr/local/share/plexmediaserver/Resources"
plexmediaserver_pbi_path=/usr/pbi/plexmediaserver-$(uname -m)/
plexmediaserver_plexdata="${plexmediaserver_pbi_path}/plexdata"
plexmediaserver_pms="${plexmediaserver_plexdata}/Plex Media Server"
plexmediaserver_media="${plexmediaserver_pms}/Media"
plexmediaserver_databases="${plexmediaserver_pms}/Plug-in Support/Databases"
plexmediaserver_library="${plexmediaserver_pms}/Library"
plexmediaserver_fonts="${plexmediaserver_library}/Fonts"

if [ -d "${plexmediaserver_plexdata}" ]
then
	mv "${plexmediaserver_plexdata}" "${plexmediaserver_plexdata}.save"
fi
