#!/bin/sh

plexmediaserver_pbi_path=/usr/pbi/plexmediaserver-$(uname -m)/

${plexmediaserver_pbi_path}/bin/python2.7 ${plexmediaserver_pbi_path}/plexmediaserverUI/manage.py syncdb --migrate --noinput
