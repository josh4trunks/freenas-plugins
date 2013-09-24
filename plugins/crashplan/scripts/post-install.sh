#!/bin/sh
#########################################

crashplan_pbi_path=/usr/pbi/crashplan-$(uname -m)

/bin/cp ${owncloud_pbi_path}/etc/rc.d/crashplan /usr/local/etc/rc.d/

${crashplan_pbi_path}/bin/python ${crashplan_pbi_path}/crashplanUI/manage.py syncdb --migrate --noinput
