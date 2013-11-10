#!/bin/sh

sickbeard_pbi_path=/usr/pbi/sickbeard-$(uname -m)

${sickbeard_pbi_path}/bin/python ${sickbeard_pbi_path}/sickbeardUI/manage.py syncdb --migrate --noinput
