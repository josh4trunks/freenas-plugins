#!/bin/sh
#########################################

sonarr_pbi_path=/usr/pbi/sonarr-$(uname -m)

${sonarr_pbi_path}/etc/rc.d/sonarr forcestop 2>/dev/null || true
