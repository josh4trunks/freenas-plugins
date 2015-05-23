#!/bin/sh
#########################################

pyload_pbi_path=/usr/pbi/pyload-$(uname -m)

${pyload_pbi_path}/bin/python2.7 ${pyload_pbi_path}/pyloadUI/manage.py syncdb --migrate --noinput

# Temporary workaround for a valid certificate store
ln -s /usr/local/share/certs/ca-root-nss.crt /etc/ssl/cert.pem
mkdir -p /usr/local/openssl
ln -s /usr/local/share/certs/ca-root-nss.crt /usr/local/openssl/cert.pem
