#!/bin/sh
# PBI building script
# This will run after your port build is complete
##############################################################################

sabnzbd_pbi_path=/usr/pbi/sabnzbd-$(uname -m)

find ${sabnzbd_pbi_path}/lib -iname "*.a" -delete
rm -rf ${sabnzbd_pbi_path}/share/doc
rm -rf ${sabnzbd_pbi_path}/share/emacs
rm -rf ${sabnzbd_pbi_path}/share/examples
rm -rf ${sabnzbd_pbi_path}/share/gettext
