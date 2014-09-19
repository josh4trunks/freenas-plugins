#!/bin/sh

mineos_pbi_path=/usr/pbi/mineos-$(uname -m)

${mineos_pbi_path}/bin/python2.7 ${mineos_pbi_path}/mineosUI/manage.py syncdb --migrate --noinput

mkdir -p /usr/compat/linux/proc /var/games/minecraft/profiles
install -o mcserver /dev/null /var/games/minecraft/profiles/profile.config
echo 'mcserver' | pw mod user mcserver -h 0
