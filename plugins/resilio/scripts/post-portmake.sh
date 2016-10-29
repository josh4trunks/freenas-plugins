#!/bin/sh
# PBI building script
# This will run after your port build is complete
##############################################################################

resilio_pbi_path=/usr/pbi/resilio-$(uname -m)

find ${resilio_pbi_path}/lib -iname "*.a" -delete
rm -rf ${resilio_pbi_path}/share/doc
rm -rf ${resilio_pbi_path}/share/emacs
rm -rf ${resilio_pbi_path}/share/examples
rm -rf ${resilio_pbi_path}/share/gettext
