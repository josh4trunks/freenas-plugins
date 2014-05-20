#!/bin/sh

syncthing_pbi_path=/usr/pbi/syncthing-$(uname -m)
${syncthing_pbi_path}/etc/rc.d/syncthing forcestop
if cmp -s ${syncthing_pbi_path}/etc/syncthing.xml.sample /var/db/syncthing/config.xml; then rm -f /var/db/syncthing/config.xml; fi
