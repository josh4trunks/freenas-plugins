#!/bin/sh
#########################################

resilio_pbi_path=/usr/pbi/resilio-$(uname -m)

${resilio_pbi_path}/bin/python2.7 ${resilio_pbi_path}/resilioUI/manage.py syncdb --migrate --noinput

install -o resilio -g resilio -d /var/db/resilio
