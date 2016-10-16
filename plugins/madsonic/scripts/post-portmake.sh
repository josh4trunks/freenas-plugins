#!/bin/sh
# PBI building script
# This will run after your port build is complete
##############################################################################

madsonic_pbi_path=/usr/pbi/madsonic-$(uname -m)

find ${madsonic_pbi_path}/lib -iname "*.a" -delete
rm -rf ${madsonic_pbi_path}/share/doc
rm -rf ${madsonic_pbi_path}/share/emacs
rm -rf ${madsonic_pbi_path}/share/examples
rm -rf ${madsonic_pbi_path}/share/gettext
