#!/bin/sh
# PBI building script
# This will run after your port build is complete
##############################################################################

syncthing_pbi_path=/usr/pbi/syncthing-$(uname -m)

find ${syncthing_pbi_path}/lib -iname "*.a" -delete
rm -rf ${syncthing_pbi_path}/share/doc
rm -rf ${syncthing_pbi_path}/share/emacs
rm -rf ${syncthing_pbi_path}/share/examples
rm -rf ${syncthing_pbi_path}/share/gettext
