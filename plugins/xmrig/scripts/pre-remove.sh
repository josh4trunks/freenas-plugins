#!/bin/sh
#########################################

xmrig_pbi_path=/usr/pbi/xmrig-$(uname -m)

${xmrig_pbi_path}/etc/rc.d/xmrig forcestop 2>/dev/null || true
