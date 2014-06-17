#!/bin/sh

xdm_pbi_path=/usr/pbi/xdm-$(uname -m)

${xdm_pbi_path}/bin/python2.7 ${xdm_pbi_path}/xdmUI/manage.py syncdb --migrate --noinput

####
mkdir -p /var/db/xdm
chown -R media:media /var/db/xdm
####
