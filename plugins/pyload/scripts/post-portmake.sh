#!/bin/sh
# PBI building script
# This will run after your port build is complete
##############################################################################

pyload_pbi_path=/usr/pbi/pyload-$(uname -m)

find ${pyload_pbi_path}/lib -iname "*.a" -delete
rm -rf ${pyload_pbi_path}/share/doc
rm -rf ${pyload_pbi_path}/share/emacs
rm -rf ${pyload_pbi_path}/share/examples
rm -rf ${pyload_pbi_path}/share/gettext
