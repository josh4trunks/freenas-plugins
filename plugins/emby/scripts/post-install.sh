#!/bin/sh
#########################################

emby_pbi_path=/usr/pbi/emby-$(uname -m)

${emby_pbi_path}/bin/python2.7 ${emby_pbi_path}/embyUI/manage.py syncdb --migrate --noinput

${emby_pbi_path}/etc/rc.d/emby-server start
