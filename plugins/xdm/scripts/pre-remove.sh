#!/bin/sh
#########################################

xdm_pbi_path=/usr/pbi/xdm-$(uname -m)

${xdm_pbi_path}/etc/rc.d/xdm forcestop 2>/dev/null || true
