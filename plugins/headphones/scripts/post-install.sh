#!/bin/sh
#########################################

headphones_pbi_path=/usr/pbi/headphones-$(uname -m)

${headphones_pbi_path}/bin/python2.7 ${headphones_pbi_path}/headphonesUI/manage.py syncdb --migrate --noinput

#Temporary Workaround
mv ${headphones_pbi_path}/etc/headphones /var/db/headphones
