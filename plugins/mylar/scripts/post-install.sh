#!/bin/sh
#########################################

mylar_pbi_path=/usr/pbi/mylar-$(uname -m)

${mylar_pbi_path}/bin/python2.7 ${mylar_pbi_path}/mylarUI/manage.py syncdb --migrate --noinput

#Temporary Workaround
mv ${mylar_pbi_path}/etc/mylar /var/db/mylar
