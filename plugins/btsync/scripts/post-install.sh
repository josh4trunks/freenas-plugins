#!/bin/sh

btsync_pbi_path=/usr/pbi/btsync-$(uname -m)

${btsync_pbi_path}/bin/python2.7 ${btsync_pbi_path}/btsyncUI/manage.py syncdb --migrate --noinput

####
mkdir -p /var/db/btsync
chown -R sync:sync /var/db/btsync
####
