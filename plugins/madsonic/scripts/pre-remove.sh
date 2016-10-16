#!/bin/sh
#########################################

madsonic_pbi_path=/usr/pbi/madsonic-$(uname -m)

${madsonic_pbi_path}/etc/rc.d/madsonic forcestop 2>/dev/null || true
