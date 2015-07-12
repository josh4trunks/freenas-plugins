#!/bin/sh
#########################################

transmission_pbi_path=/usr/pbi/transmission-$(uname -m)

${transmission_pbi_path}/bin/python2.7 ${transmission_pbi_path}/transmissionUI/manage.py syncdb --migrate --noinput

sysrc 'transmission_conf_dir=/var/db/transmission' 'transmission_download_dir='
