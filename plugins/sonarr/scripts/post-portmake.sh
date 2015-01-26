#!/bin/sh
# PBI building script
# This will run after your port build is complete
##############################################################################

sonarr_pbi_path=/usr/pbi/sonarr-$(uname -m)

find ${sonarr_pbi_path}/lib -iname "*.a" -delete
rm -rf ${sonarr_pbi_path}/share/doc
rm -rf ${sonarr_pbi_path}/share/emacs
rm -rf ${sonarr_pbi_path}/share/examples
rm -rf ${sonarr_pbi_path}/share/gettext
