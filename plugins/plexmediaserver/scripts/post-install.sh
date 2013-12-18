#!/bin/sh
#########################################

plexmediaserver_resources="/usr/local/share/plexmediaserver/Resources"
plexmediaserver_pbi_path=/usr/pbi/plexmediaserver-$(uname -m)/
plexmediaserver_plexdata="${plexmediaserver_pbi_path}/plexdata"
plexmediaserver_pms="${plexmediaserver_plexdata}/Plex Media Server"
plexmediaserver_media="${plexmediaserver_pms}/Media"
plexmediaserver_databases="${plexmediaserver_pms}/Plug-in Support/Databases"

plexmediaserver_library="${plexmediaserver_pms}/Library"
plexmediaserver_fonts="${plexmediaserver_library}/Fonts"

pw group add plex
pw user add plex -g plex -d "${plexmediaserver_pbi_path}"

mkdir -p "${plexmediaserver_media}/Movies"
mkdir -p "${plexmediaserver_media}/TV Shows"
mkdir -p "${plexmediaserver_media}/Music"
mkdir -p "${plexmediaserver_media}/Photos"
mkdir -p "${plexmediaserver_media}/Home Movies"

mkdir -p "${plexmediaserver_fonts}"
cp "${plexmediaserver_resources}/DejaVuUniversal.ttf" "${plexmediaserver_fonts}/Unicode.ttf" 
cp "${plexmediaserver_resources}/DejaVuUniversal.ttf" "${plexmediaserver_fonts}/Arial.ttf"

${plexmediaserver_pbi_path}/bin/python ${plexmediaserver_pbi_path}/plexmediaserverUI/manage.py syncdb --migrate --noinput
~
cp ${plexmediaserver_pbi_path}/etc/rc.d/plexmediaserver /usr/local/etc/rc.d/plexmediaserver

echo "Changing ownership of ${plexmediaserver_plexdata} to $(id plex)"
chown -R plex:plex "${plexmediaserver_plexdata}"
chmod 644 "${plexmediaserver_databases}"/com*
