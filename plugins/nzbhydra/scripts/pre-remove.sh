#!/bin/sh
#########################################

nzbhydra_pbi_path=/usr/pbi/nzbhydra-$(uname -m)

${nzbhydra_pbi_path}/etc/rc.d/nzbhydra forcestop 2>/dev/null || true
