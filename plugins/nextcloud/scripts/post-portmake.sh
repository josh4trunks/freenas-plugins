#!/bin/sh
# PBI building script
# This will run after your port build is complete
##############################################################################

nextcloud_pbi_path=/usr/pbi/nextcloud-$(uname -m)/

find ${nextcloud_pbi_path}/lib -iname "*.a" -delete
rm -rf ${nextcloud_pbi_path}/share/doc
rm -rf ${nextcloud_pbi_path}/share/emacs
rm -rf ${nextcloud_pbi_path}/share/examples
rm -rf ${nextcloud_pbi_path}/share/gettext
