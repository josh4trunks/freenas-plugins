#!/bin/sh

syncthing_pbi_path=/usr/pbi/syncthing-$(uname -m)

${syncthing_pbi_path}/bin/python2.7 ${syncthing_pbi_path}/syncthingUI/manage.py syncdb --migrate --noinput

install -o syncthing -g syncthing -d /var/db/syncthing
if [ ! -f /var/db/syncthing/config.xml ] ; then install -o syncthing -g syncthing ${syncthing_pbi_path}/etc/syncthing.xml.sample /var/db/syncthing/config.xml; fi
