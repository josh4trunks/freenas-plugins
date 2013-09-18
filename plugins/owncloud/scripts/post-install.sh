#!/bin/sh
#########################################

owncloud_pbi_path=/usr/pbi/owncloud-$(uname -m)/

${owncloud_pbi_path}/bin/python ${owncloud_pbi_path}/owncloudUI/manage.py syncdb --migrate --noinput
