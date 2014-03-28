#!/bin/sh

mineos_pbi_path=/usr/pbi/mineos-$(uname -m)

${mineos_pbi_path}/bin/python2.7 ${mineos_pbi_path}/mineosUI/manage.py syncdb --migrate --noinput

####
mkdir -p /usr/compat/linux/proc
pw adduser mcserver -d /nonexistent -s /usr/sbin/nologin
echo 'mcpass' | pw mod user mcserver -h 0
mkdir -p /var/games/minecraft/profiles && touch /var/games/minecraft/profiles/profile.config
chown mcserver /var/games/minecraft/profiles/profile.config
####
