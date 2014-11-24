#!/bin/sh
#########################################

mineos_pbi_path=/usr/pbi/mineos-$(uname -m)

${mineos_pbi_path}/etc/rc.d/mineos forcestop 2>/dev/null || true
