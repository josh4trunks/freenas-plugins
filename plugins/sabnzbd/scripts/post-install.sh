#!/bin/sh

sabnzbd_pbi_path=/usr/pbi/sabnzbd-$(uname -m)

${sabnzbd_pbi_path}/bin/python ${sabnzbd_pbi_path}/sabnzbdUI/manage.py syncdb --migrate --noinput
