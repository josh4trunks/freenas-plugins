#!/bin/sh
#########################################

sabnzbd_pbi_path=/usr/pbi/sabnzbd-$(uname -m)

${sabnzbd_pbi_path}/bin/python2.7 ${sabnzbd_pbi_path}/sabnzbdUI/manage.py syncdb --migrate --noinput

# Temporary workaround for a valid certificate store
ln -s /usr/local/share/certs/ca-root-nss.crt /etc/ssl/cert.pem
mkdir -p ${sabnzbd_pbi_path}/openssl
ln -s /usr/local/share/certs/ca-root-nss.crt ${sabnzbd_pbi_path}/openssl/cert.pem

sysrc 'sabnzbd_conf_dir=/var/db/sabnzbd'
# Temporary workaround, create and set Sabnzbd's user as 'media'
if [ ! -d /var/db/sabnzbd ]; then
	pw useradd -n media -u 816 -d /nonexistent -s /sbin/nologin
fi
sysrc 'sabnzbd_user=media'
