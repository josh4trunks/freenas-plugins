#!/bin/sh
#########################################

sickrage_pbi_path=/usr/pbi/sickrage-$(uname -m)

${sickrage_pbi_path}/bin/python2.7 ${sickrage_pbi_path}/sickrageUI/manage.py syncdb --migrate --noinput

# Temporary workaround for a valid certificate store
ln -s /usr/local/share/certs/ca-root-nss.crt /etc/ssl/cert.pem
mkdir -p ${sickrage_pbi_path}/openssl
ln -s /usr/local/share/certs/ca-root-nss.crt ${sickrage_pbi_path}/openssl/cert.pem
