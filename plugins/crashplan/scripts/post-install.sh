#!/bin/sh
#########################################

crashplan_pbi_path=/usr/pbi/crashplan-$(uname -m)

/bin/cp ${crashplan_pbi_path}/etc/rc.d/crashplan /usr/local/etc/rc.d/

mkdir -p /compat/linux
ln -sf ${crashplan_pbi_path}/linuxlib /compat/linux/lib

#For some reason the default relative RPATH doesnt work in java bin
${crashplan_pbi_path}/bin/patchelf \
	--set-rpath ${crashplan_pbi_path}/linux-sun-jre1.6.0/lib/i386/jli \
	${crashplan_pbi_path}/linux-sun-jre1.6.0/bin/java

${crashplan_pbi_path}/bin/python ${crashplan_pbi_path}/crashplanUI/manage.py syncdb --migrate --noinput
