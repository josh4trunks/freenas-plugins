#!/bin/sh
# PBI building script
# This will run after your port build is complete
##############################################################################

emby_pbi_path=/usr/pbi/emby-$(uname -m)

find ${emby_pbi_path}/lib -iname "*.a" -delete
rm -rf ${emby_pbi_path}/share/doc
rm -rf ${emby_pbi_path}/share/emacs
rm -rf ${emby_pbi_path}/share/examples
rm -rf ${emby_pbi_path}/share/gettext
