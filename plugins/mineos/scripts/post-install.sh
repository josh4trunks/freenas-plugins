#!/bin/sh
#########################################

mineos_pbi_path=/usr/pbi/mineos-$(uname -m)

${mineos_pbi_path}/bin/python2.7 ${mineos_pbi_path}/mineosUI/manage.py syncdb --migrate --noinput

if [ ! -d /usr/compat/linux/proc ]; then
	mkdir -p /usr/compat/linux/proc

	export O=FreeNAS
	/bin/sh ${mineos_pbi_path}/share/mineos/mineos-node/generate-sslcert.sh

	echo 'mcserver' | pw useradd -n mcserver -u 199 -d /nonexistent -s /bin/sh -h 0
fi
