#!/bin/sh
# PBI building script
# This will run after your port build is complete
##############################################################################

btsync_pbi_path=/usr/pbi/btsync-$(uname -m)

find ${btsync_pbi_path}/lib -iname "*.a" -delete
rm -rf ${btsync_pbi_path}/share/doc
rm -rf ${btsync_pbi_path}/share/emacs
rm -rf ${btsync_pbi_path}/share/examples
rm -rf ${btsync_pbi_path}/share/gettext
