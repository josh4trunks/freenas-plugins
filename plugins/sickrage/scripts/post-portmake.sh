#!/bin/sh
# PBI building script
# This will run after your port build is complete
##############################################################################

sickrage_pbi_path=/usr/pbi/sickrage-$(uname -m)

find ${sickrage_pbi_path}/lib -iname "*.a" -delete
rm -rf ${sickrage_pbi_path}/share/doc
rm -rf ${sickrage_pbi_path}/share/emacs
rm -rf ${sickrage_pbi_path}/share/examples
rm -rf ${sickrage_pbi_path}/share/gettext
