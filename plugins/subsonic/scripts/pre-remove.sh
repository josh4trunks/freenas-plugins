#!/bin/sh
#########################################

subsonic_pbi_path=/usr/pbi/subsonic-$(uname -m)

${subsonic_pbi_path}/etc/rc.d/subsonic forcestop 2>/dev/null || true
