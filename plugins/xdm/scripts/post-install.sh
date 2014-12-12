#!/bin/sh
#########################################

xdm_pbi_path=/usr/pbi/xdm-$(uname -m)

${xdm_pbi_path}/bin/python2.7 ${xdm_pbi_path}/xdmUI/manage.py syncdb --migrate --noinput

#Temporary Workaround
mv ${xdm_pbi_path}/etc/xdm /var/db/xdm
