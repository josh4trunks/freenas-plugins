#!/bin/sh
#########################################

mineos_pbi_path=/usr/pbi/mineos-$(uname -m)

${mineos_pbi_path}/bin/python2.7 ${mineos_pbi_path}/mineosUI/manage.py syncdb --migrate --noinput

# Temporary workaround for a valid certificate store
ln -s /usr/local/share/certs/ca-root-nss.crt /etc/ssl/cert.pem
mkdir -p ${mineos_pbi_path}/openssl
ln -s /usr/local/share/certs/ca-root-nss.crt ${mineos_pbi_path}/openssl/cert.pem

mkdir -p /usr/compat/linux/proc /var/games/minecraft/profiles
install -g mcserver /dev/null /var/games/minecraft/profiles/profile.config

# Set default password only if it isn't set
PASSWD_HASH=$(cat /etc/master.passwd | grep -e "^mcserver" | sed -e "s/^mcserver:\([^:]*\):.*$/\1/")
if [ "${PASSWD_HASH}" = "*" ]; then
	echo 'mcserver' | pw mod user mcserver -h 0
fi

${mineos_pbi_path}/etc/rc.d/mineos start
