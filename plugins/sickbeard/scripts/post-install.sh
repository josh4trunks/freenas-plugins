#!/bin/sh
#########################################

sickbeard_pbi_path=/usr/pbi/sickbeard-$(uname -m)

${sickbeard_pbi_path}/bin/python2.7 ${sickbeard_pbi_path}/sickbeardUI/manage.py syncdb --migrate --noinput

# Temporary workaround for a valid certificate store
ln -s /usr/local/share/certs/ca-root-nss.crt /etc/ssl/cert.pem
mkdir -p ${sickbeard_pbi_path}/openssl
ln -s /usr/local/share/certs/ca-root-nss.crt ${sickbeard_pbi_path}/openssl/cert.pem
