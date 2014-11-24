#!/bin/sh
# PBI building script
# This will run after your port build is complete
##############################################################################

headphones_pbi_path=/usr/pbi/headphones-$(uname -m)

find ${headphones_pbi_path}/lib -iname "*.a" -delete
rm -rf ${headphones_pbi_path}/share/doc
rm -rf ${headphones_pbi_path}/share/emacs
rm -rf ${headphones_pbi_path}/share/examples
rm -rf ${headphones_pbi_path}/share/gettext
