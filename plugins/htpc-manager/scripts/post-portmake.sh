#!/bin/sh
# PBI building script
# This will run after your port build is complete
##############################################################################

htpc_manager_pbi_path=/usr/pbi/htpc_manager-$(uname -m)

find ${htpc_manager_pbi_path}/lib -iname "*.a" -delete
rm -rf ${htpc_manager_pbi_path}/share/doc
rm -rf ${htpc_manager_pbi_path}/share/emacs
rm -rf ${htpc_manager_pbi_path}/share/examples
rm -rf ${htpc_manager_pbi_path}/share/gettext
