#!/bin/sh
#########################################

sickrage_pbi_path=/usr/pbi/sickrage-$(uname -m)

${sickrage_pbi_path}/bin/python2.7 ${sickrage_pbi_path}/sickrageUI/manage.py syncdb --migrate --noinput
