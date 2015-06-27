#!/bin/sh
#########################################

pyload_pbi_path=/usr/pbi/pyload-$(uname -m)

${pyload_pbi_path}/bin/python2.7 ${pyload_pbi_path}/pyloadUI/manage.py syncdb --migrate --noinput

# Temporary workaround for a valid certificate store
ln -s /usr/local/share/certs/ca-root-nss.crt /etc/ssl/cert.pem
mkdir -p ${pyload_pbi_path}/openssl
ln -s /usr/local/share/certs/ca-root-nss.crt ${pyload_pbi_path}/openssl/cert.pem
