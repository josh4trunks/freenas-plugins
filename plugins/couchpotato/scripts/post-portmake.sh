#!/bin/sh
# PBI building script
# This will run after your port build is complete
##############################################################################

couchpotato_pbi_path=/usr/pbi/couchpotato-$(uname -m)

find ${couchpotato_pbi_path}/lib -iname "*.a" -delete
rm -rf ${couchpotato_pbi_path}/share/doc
rm -rf ${couchpotato_pbi_path}/share/emacs
rm -rf ${couchpotato_pbi_path}/share/examples
rm -rf ${couchpotato_pbi_path}/share/gettext
