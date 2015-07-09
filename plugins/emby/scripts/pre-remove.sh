#!/bin/sh
#########################################

emby_pbi_path=/usr/pbi/emby-$(uname -m)

${emby_pbi_path}/etc/rc.d/emby-server forcestop 2>/dev/null || true
