#!/bin/sh
#########################################

emby_pbi_path=/usr/pbi/emby-$(uname -m)

${emby_pbi_path}/bin/python2.7 ${emby_pbi_path}/embyUI/manage.py syncdb --migrate --noinput

# Rename mediabrowser group and user to emby
if [ $(id -u mediabrowser) -eq 989 ]; then
	pw groupmod 989 -n mediabrowser -l emby;
	pw usermod 989 -n mediabrowser -l emby -g emby -c Emby\ Server;
fi
