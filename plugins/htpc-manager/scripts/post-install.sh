#!/bin/sh
#########################################

htpc_manager_pbi_path=/usr/pbi/htpc-manager-$(uname -m)

${htpc_manager_pbi_path}/bin/python2.7 ${htpc_manager_pbi_path}/htpcmanagerUI/manage.py syncdb --migrate --noinput

# Temporary workaround for a valid certificate store
ln -s /usr/local/share/certs/ca-root-nss.crt /etc/ssl/cert.pem
mkdir -p /usr/local/openssl
ln -s /usr/local/share/certs/ca-root-nss.crt /usr/local/openssl/cert.pem
