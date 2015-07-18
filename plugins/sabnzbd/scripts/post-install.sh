#!/bin/sh
#########################################

sabnzbd_pbi_path=/usr/pbi/sabnzbd-$(uname -m)

${sabnzbd_pbi_path}/bin/python2.7 ${sabnzbd_pbi_path}/sabnzbdUI/manage.py syncdb --migrate --noinput

# Temporary workaround for a valid certificate store
ln -s /usr/local/share/certs/ca-root-nss.crt /etc/ssl/cert.pem
mkdir -p ${sabnzbd_pbi_path}/openssl
ln -s /usr/local/share/certs/ca-root-nss.crt ${sabnzbd_pbi_path}/openssl/cert.pem

rm ${sabnzbd_pbi_path}/etc/avahi/services/sftp-ssh.service ${sabnzbd_pbi_path}/etc/avahi/services/ssh.service
sysrc 'dbus_enable=YES' 'avahi_daemon_enable=YES'
${sabnzbd_pbi_path}/etc/rc.d/dbus start
${sabnzbd_pbi_path}/etc/rc.d/avahi-daemon start
