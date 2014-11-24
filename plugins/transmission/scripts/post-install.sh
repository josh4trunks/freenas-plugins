#!/bin/sh
#########################################

transmission_pbi_path=/usr/pbi/transmission-$(uname -m)

${transmission_pbi_path}/bin/python2.7 ${transmission_pbi_path}/transmissionUI/manage.py syncdb --migrate --noinput

sed -i '' -e '/^start_precmd=transmission_prestart$/ a\
extra_commands="reload"' ${transmission_pbi_path}/etc/rc.d/transmission

sysrc 'transmission_download_dir='
