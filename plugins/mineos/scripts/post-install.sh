#!/bin/sh
#########################################

mineos_pbi_path=/usr/pbi/mineos-$(uname -m)

${mineos_pbi_path}/bin/python2.7 ${mineos_pbi_path}/mineosUI/manage.py syncdb --migrate --noinput

# Temporary workaround for a valid certificate store
ln -s /usr/local/share/certs/ca-root-nss.crt /etc/ssl/cert.pem
mkdir -p /usr/local/openssl
ln -s /usr/local/share/certs/ca-root-nss.crt /usr/local/openssl/cert.pem

mkdir -p /usr/compat/linux/proc /var/games/minecraft/profiles
install -g mcserver /dev/null /var/games/minecraft/profiles/profile.config
echo 'mcserver' | pw mod user mcserver -h 0
