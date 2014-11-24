#!/bin/sh
# PBI building script
# This will run after your port build is complete
##############################################################################

sickbeard_pbi_path=/usr/pbi/sickbeard-$(uname -m)

find ${sickbeard_pbi_path}/lib -iname "*.a" -delete
rm -rf ${sickbeard_pbi_path}/share/doc
rm -rf ${sickbeard_pbi_path}/share/emacs
rm -rf ${sickbeard_pbi_path}/share/examples
rm -rf ${sickbeard_pbi_path}/share/gettext
