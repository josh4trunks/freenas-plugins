#!/bin/sh
# PBI building script
# This will run after your port build is complete
##############################################################################

owncloud_pbi_path=/usr/pbi/owncloud-$(uname -m)/

find ${owncloud_pbi_path}/lib -iname "*.a" -delete
rm -rf ${owncloud_pbi_path}/share/doc
rm -rf ${owncloud_pbi_path}/share/emacs
rm -rf ${owncloud_pbi_path}/share/examples
rm -rf ${owncloud_pbi_path}/share/gettext
