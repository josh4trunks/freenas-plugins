#!/bin/sh
#########################################

btsync_pbi_path=/usr/pbi/btsync-$(uname -m)

${btsync_pbi_path}/etc/rc.d/btsync forcestop 2>/dev/null || true
