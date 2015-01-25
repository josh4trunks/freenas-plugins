#!/bin/sh
# PBI building script
# This will run after your port build is complete
##############################################################################

mineos_pbi_path=/usr/pbi/mineos-$(uname -m)

find ${mineos_pbi_path}/lib -iname "*.a" -delete
rm -rf ${mineos_pbi_path}/share/doc
rm -rf ${mineos_pbi_path}/share/emacs
rm -rf ${mineos_pbi_path}/share/examples
rm -rf ${mineos_pbi_path}/share/gettext
