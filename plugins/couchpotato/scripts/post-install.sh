#!/bin/sh
#########################################

couchpotato_pbi_path=/usr/pbi/couchpotato-$(uname -m)

${couchpotato_pbi_path}/bin/python2.7 ${couchpotato_pbi_path}/couchpotatoUI/manage.py syncdb --migrate --noinput
