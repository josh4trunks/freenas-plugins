#!/bin/sh
#########################################

xdm_pbi_path=/usr/pbi/xdm-$(uname -m)

${xdm_pbi_path}/bin/python2.7 ${xdm_pbi_path}/xdmUI/manage.py syncdb --migrate --noinput

# Temporary workaround for a valid certificate store
ln -s /usr/local/share/certs/ca-root-nss.crt /etc/ssl/cert.pem
mkdir -p ${xdm_pbi_path}/openssl
ln -s /usr/local/share/certs/ca-root-nss.crt ${xdm_pbi_path}/openssl/cert.pem
