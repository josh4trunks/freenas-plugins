#!/bin/sh
# PBI building script
# This will run after your port build is complete
##############################################################################

xmrig_pbi_path=/usr/pbi/xmrig-$(uname -m)

find ${xmrig_pbi_path}/lib -iname "*.py[co]" -delete
find ${xmrig_pbi_path}/lib -iname "*.a" -delete
rm -rf ${xmrig_pbi_path}/share/doc
rm -rf ${xmrig_pbi_path}/share/emacs
rm -rf ${xmrig_pbi_path}/share/examples
rm -rf ${xmrig_pbi_path}/share/gettext
