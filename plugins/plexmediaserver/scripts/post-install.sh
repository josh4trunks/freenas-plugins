#!/bin/sh
#########################################

plexmediaserver_pbi_path=/usr/pbi/plexmediaserver-$(uname -m)

${plexmediaserver_pbi_path}/bin/python2.7 ${plexmediaserver_pbi_path}/plexmediaserverUI/manage.py syncdb --migrate --noinput

sysrc 'plexmediaserver_support_path=/var/db/plexdata'

${plexmediaserver_pbi_path}/etc/rc.d/plexmediaserver start
