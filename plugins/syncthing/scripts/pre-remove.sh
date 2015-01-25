#!/bin/sh
#########################################

syncthing_pbi_path=/usr/pbi/syncthing-$(uname -m)

${syncthing_pbi_path}/etc/rc.d/syncthing forcestop 2>/dev/null || true
