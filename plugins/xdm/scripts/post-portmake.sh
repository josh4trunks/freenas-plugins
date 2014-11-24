#!/bin/sh
# PBI building script
# This will run after your port build is complete
##############################################################################

xdm_pbi_path=/usr/pbi/xdm-$(uname -m)

find ${xdm_pbi_path}/lib -iname "*.a" -delete
rm -rf ${xdm_pbi_path}/share/doc
rm -rf ${xdm_pbi_path}/share/emacs
rm -rf ${xdm_pbi_path}/share/examples
rm -rf ${xdm_pbi_path}/share/gettext
