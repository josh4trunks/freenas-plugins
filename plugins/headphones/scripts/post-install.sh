#!/bin/sh
#########################################

headphones_pbi_path=/usr/pbi/headphones-$(uname -m)

${headphones_pbi_path}/bin/python2.7 ${headphones_pbi_path}/headphonesUI/manage.py syncdb --migrate --noinput

# Temporary workaround for a valid certificate store
ln -s /usr/local/share/certs/ca-root-nss.crt /etc/ssl/cert.pem
mkdir -p ${headphones_pbi_path}/openssl
ln -s /usr/local/share/certs/ca-root-nss.crt ${headphones_pbi_path}/openssl/cert.pem
