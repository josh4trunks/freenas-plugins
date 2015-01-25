#!/bin/sh
# PBI building script
# This will run after your port build is complete
##############################################################################

lazylibrarian_pbi_path=/usr/pbi/lazylibrarian-$(uname -m)

find ${lazylibrarian_pbi_path}/lib -iname "*.a" -delete
rm -rf ${lazylibrarian_pbi_path}/share/doc
rm -rf ${lazylibrarian_pbi_path}/share/emacs
rm -rf ${lazylibrarian_pbi_path}/share/examples
rm -rf ${lazylibrarian_pbi_path}/share/gettext
