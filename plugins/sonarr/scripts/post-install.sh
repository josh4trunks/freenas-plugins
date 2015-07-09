#!/bin/sh
#########################################

sonarr_pbi_path=/usr/pbi/sonarr-$(uname -m)

${sonarr_pbi_path}/bin/python2.7 ${sonarr_pbi_path}/sonarrUI/manage.py syncdb --migrate --noinput

${sonarr_pbi_path}/etc/rc.d/sonarr start
