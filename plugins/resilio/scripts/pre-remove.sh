#!/bin/sh
#########################################

resilio_pbi_path=/usr/pbi/resilio-$(uname -m)

${resilio_pbi_path}/etc/rc.d/resilio forcestop 2>/dev/null || true
