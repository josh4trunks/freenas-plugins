#!/bin/sh
#########################################

mylar_pbi_path=/usr/pbi/mylar-$(uname -m)

${mylar_pbi_path}/etc/rc.d/mylar forcestop 2>/dev/null || true
