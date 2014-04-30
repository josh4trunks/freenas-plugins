#!/bin/sh

htpc_manager_pbi_path=/usr/pbi/htpc-manager-$(uname -m)

${htpc_manager_pbi_path}/bin/python2.7 ${htpc_manager_pbi_path}/htpcmanagerUI/manage.py syncdb --migrate --noinput

####
mkdir -p /var/db/htpc-manager
chown -R media:media /var/db/htpc-manager
####
