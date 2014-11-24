#!/bin/sh
# PBI building script
# This will run after your port build is complete
##############################################################################

mylar_pbi_path=/usr/pbi/mylar-$(uname -m)

find ${mylar_pbi_path}/lib -iname "*.a" -delete
rm -rf ${mylar_pbi_path}/share/doc
rm -rf ${mylar_pbi_path}/share/emacs
rm -rf ${mylar_pbi_path}/share/examples
rm -rf ${mylar_pbi_path}/share/gettext
