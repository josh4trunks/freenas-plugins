#!/bin/sh
#########################################

emby_pbi_path=/usr/pbi/emby-$(uname -m)

${emby_pbi_path}/bin/python2.7 ${emby_pbi_path}/embyUI/manage.py syncdb --migrate --noinput

# Install fonts config if it doesn't exist
if [ ! -f /usr/local/etc/fonts/fonts.conf ]; then
	mkdir -p /usr/local/etc/fonts
	cat << __EOF__ > /usr/local/etc/fonts/fonts.conf
<?xml version="1.0"?>
<fontconfig>
	<dir>/usr/local/lib/X11/fonts</dir>
</fontconfig>
__EOF__
fi

# Install library if it doesn't exist
if [ ! -f /usr/local/lib/libiconv.so.3 ]; then
	 ln -s ${emby_pbi_path}/lib/libiconv.so.3 /usr/local/lib
fi
