#!/bin/sh
# PBI building script
# This will run after your port build is complete
##############################################################################

mediabrowser_pbi_path=/usr/pbi/mediabrowser-$(uname -m)

find ${mediabrowser_pbi_path}/lib -iname "*.a" -delete
rm -rf ${mediabrowser_pbi_path}/share/doc
rm -rf ${mediabrowser_pbi_path}/share/emacs
rm -rf ${mediabrowser_pbi_path}/share/examples
rm -rf ${mediabrowser_pbi_path}/share/gettext
