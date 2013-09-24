#!/bin/sh
# PBI building script
# This will run after your port build is complete
##############################################################################

crashplan_pbi_path=/usr/pbi/crashplan-$(uname -m)/

find ${crashplan_pbi_path}/lib -iname "*.a" -delete
rm -rf ${crashplan_pbi_path}/share/doc
rm -rf ${crashplan_pbi_path}/share/emacs
rm -rf ${crashplan_pbi_path}/share/examples
rm -rf ${crashplan_pbi_path}/share/gettext
