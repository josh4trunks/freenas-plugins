#!/bin/sh
# PBI building script
# This will run after your port build is complete
##############################################################################

subsonic_pbi_path=/usr/pbi/subsonic-$(uname -m)

find ${subsonic_pbi_path}/lib -iname "*.a" -delete
rm -rf ${subsonic_pbi_path}/share/doc
rm -rf ${subsonic_pbi_path}/share/emacs
rm -rf ${subsonic_pbi_path}/share/examples
rm -rf ${subsonic_pbi_path}/share/gettext
