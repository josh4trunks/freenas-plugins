#!/bin/sh

sickbeard_pbi_path=/usr/pbi/sickbeard-$(uname -m)

${sickbeard_pbi_path}/bin/python2.7 ${sickbeard_pbi_path}/sickbeardUI/manage.py syncdb --migrate --noinput

install -o media -g media -d /var/db/sickbeard
