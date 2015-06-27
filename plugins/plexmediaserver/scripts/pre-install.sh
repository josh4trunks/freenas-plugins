#!/bin/sh
#########################################

plexmediaserver_pbi_path=/usr/pbi/plexmediaserver-$(uname -m)

if [ ! -d "/var/db/plexdata" ]; then
	if [ -d "${plexmediaserver_pbi_path}/plexdata" ]; then
		mv "${plexmediaserver_pbi_path}/plexdata" "/var/db/plexdata"
	elif [ -d "${plexmediaserver_pbi_path}/plexdata.save" ]; then
		mv "${plexmediaserver_pbi_path}/plexdata.save" "/var/db/plexdata"
	fi
fi
