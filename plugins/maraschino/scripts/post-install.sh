#!/bin/sh

maraschino_pbi_path=/usr/pbi/maraschino-$(uname -m)

${maraschino_pbi_path}/bin/python2.7 ${maraschino_pbi_path}/maraschinoUI/manage.py syncdb --migrate --noinput

####
mkdir -p /var/db/maraschino
chown -R media:media /var/db/maraschino
####
