#!/bin/sh
#########################################

mineos_pbi_path=/usr/pbi/mineos-$(uname -m)

${mineos_pbi_path}/bin/python2.7 ${mineos_pbi_path}/mineosUI/manage.py syncdb --migrate --noinput

mkdir -p /usr/compat/linux/proc

# Set default password only if it isn't set
PASSWD_HASH=$(cat /etc/master.passwd | grep -e "^mcserver" | sed -e "s/^mcserver:\([^:]*\):.*$/\1/")
if [ "${PASSWD_HASH}" = "*" ]; then
	echo 'mcserver' | pw mod user mcserver -h 0
fi
