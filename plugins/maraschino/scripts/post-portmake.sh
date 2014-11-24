#!/bin/sh
# PBI building script
# This will run after your port build is complete
##############################################################################

maraschino_pbi_path=/usr/pbi/maraschino-$(uname -m)

find ${maraschino_pbi_path}/lib -iname "*.a" -delete
rm -rf ${maraschino_pbi_path}/share/doc
rm -rf ${maraschino_pbi_path}/share/emacs
rm -rf ${maraschino_pbi_path}/share/examples
rm -rf ${maraschino_pbi_path}/share/gettext
