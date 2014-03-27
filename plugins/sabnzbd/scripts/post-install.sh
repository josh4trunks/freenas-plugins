#!/bin/sh

sabnzbd_pbi_path=/usr/pbi/sabnzbd-$(uname -m)

${sabnzbd_pbi_path}/bin/python2.7 ${sabnzbd_pbi_path}/sabnzbdUI/manage.py syncdb --migrate --noinput

####
mkdir -p /var/db/sabnzbd
chown -R media:media /var/db/sabnzbd
####
