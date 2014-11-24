#!/bin/sh
#########################################

mediabrowser_pbi_path=/usr/pbi/mediabrowser-$(uname -m)

${mediabrowser_pbi_path}/etc/rc.d/mediabrowser forcestop 2>/dev/null || true
