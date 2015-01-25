#!/bin/sh
#########################################

lazylibrarian_pbi_path=/usr/pbi/lazylibrarian-$(uname -m)

${lazylibrarian_pbi_path}/etc/rc.d/lazylibrarian forcestop 2>/dev/null || true
