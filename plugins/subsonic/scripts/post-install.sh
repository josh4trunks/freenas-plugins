#!/bin/sh

subsonic_pbi_path=/usr/pbi/subsonic-$(uname -m)

${subsonic_pbi_path}/bin/python2.7 ${subsonic_pbi_path}/subsonicUI/manage.py syncdb --migrate --noinput

####
mkdir -p /var/db/subsonic/transcode
ln -s ${subsonic_pbi_path}/bin/ffmpeg /var/db/subsonic/transcode/ffmpeg
chown -R media:media /var/db/subsonic
####
