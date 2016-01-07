#!/bin/sh
#########################################

sonarr_pbi_path=/usr/pbi/sonarr-$(uname -m)

${sonarr_pbi_path}/bin/python2.7 ${sonarr_pbi_path}/sonarrUI/manage.py syncdb --migrate --noinput

sysrc 'sonarr_data_dir=/var/db/sonarr'
# Temporary workaround, create and set Sonarr's user as 'media'
if [ ! -d /var/db/sonarr ]; then
	pw useradd -n media -u 816 -d /nonexistent -s /sbin/nologin
fi
sysrc 'sonarr_user=media'

# Allow Sonarr to update itself
chown -R media ${sonarr_pbi_path}/share/sonarr
