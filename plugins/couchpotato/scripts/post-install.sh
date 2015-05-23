#!/bin/sh
#########################################

couchpotato_pbi_path=/usr/pbi/couchpotato-$(uname -m)

${couchpotato_pbi_path}/bin/python2.7 ${couchpotato_pbi_path}/couchpotatoUI/manage.py syncdb --migrate --noinput

# Temporary workaround for a valid certificate store
ln -s /usr/local/share/certs/ca-root-nss.crt /etc/ssl/cert.pem
mkdir -p /usr/local/openssl
ln -s /usr/local/share/certs/ca-root-nss.crt /usr/local/openssl/cert.pem
