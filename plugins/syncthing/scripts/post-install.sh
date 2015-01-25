#!/bin/sh
#########################################

syncthing_pbi_path=/usr/pbi/syncthing-$(uname -m)

${syncthing_pbi_path}/bin/python2.7 ${syncthing_pbi_path}/syncthingUI/manage.py syncdb --migrate --noinput

# If syncthing hasn't been run before have it accept remote connections
if [ ! -f /var/db/syncthing/config.xml ]; then
	service syncthing onestart
	while [ ! -f /var/db/syncthing/config.xml ]; do
		sleep 1
	done
	service syncthing onestop
	sed -i '' -e 's|^\([[:space:]]*<address>\)127\.0\.0\.1\(:[[:digit:]]\{1,5\}</address>\)$|\10.0.0.0\2|' /var/db/syncthing/config.xml
fi
