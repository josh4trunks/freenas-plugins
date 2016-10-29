#!/bin/sh
# PBI building script
# This will run after your port build is complete
##############################################################################

nzbhydra_pbi_path=/usr/pbi/nzbhydra-$(uname -m)

find ${nzbhydra_pbi_path}/lib -iname "*.a" -delete
rm -rf ${nzbhydra_pbi_path}/share/doc
rm -rf ${nzbhydra_pbi_path}/share/emacs
rm -rf ${nzbhydra_pbi_path}/share/examples
rm -rf ${nzbhydra_pbi_path}/share/gettext
