#!/bin/sh
#########################################

sabnzbd_pbi_path=/usr/pbi/sabnzbd-$(uname -m)

${sabnzbd_pbi_path}/bin/python2.7 ${sabnzbd_pbi_path}/sabnzbdUI/manage.py syncdb --migrate --noinput

# Temporary workaround for a valid certificate store
ln -s /usr/local/share/certs/ca-root-nss.crt /etc/ssl/cert.pem
mkdir -p ${sabnzbd_pbi_path}/openssl
ln -s /usr/local/share/certs/ca-root-nss.crt ${sabnzbd_pbi_path}/openssl/cert.pem

${sabnzbd_pbi_path}/etc/rc.d/sabnzbd start
