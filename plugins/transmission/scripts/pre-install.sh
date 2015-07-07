#!/bin/sh
#########################################

transmission_pbi_path=/usr/pbi/transmission-$(uname -m)

if [ ! -d "/var/db/transmission" ]; then
	if [ -d "${transmission_pbi_path}/etc/transmission/home" ]; then
		mv "${transmission_pbi_path}/etc/transmission/home" "/var/db/transmission"
	else
		mkdir /var/db/transmission
	fi
fi
