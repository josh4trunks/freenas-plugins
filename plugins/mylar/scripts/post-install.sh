#!/bin/sh

mylar_pbi_path=/usr/pbi/mylar-$(uname -m)

${mylar_pbi_path}/bin/python2.7 ${mylar_pbi_path}/mylarUI/manage.py syncdb --migrate --noinput

####
mkdir -p /var/db/mylar
chown -R media:media /var/db/mylar
####
