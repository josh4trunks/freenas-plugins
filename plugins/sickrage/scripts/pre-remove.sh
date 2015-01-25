#!/bin/sh
#########################################

sickrage_pbi_path=/usr/pbi/sickrage-$(uname -m)

${sickrage_pbi_path}/etc/rc.d/sickrage forcestop 2>/dev/null || true
