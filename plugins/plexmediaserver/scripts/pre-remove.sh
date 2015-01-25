#!/bin/sh
#########################################

plexmediaserver_pbi_path=/usr/pbi/plexmediaserver-$(uname -m)

${plexmediaserver_pbi_path}/etc/rc.d/plexmediaserver forcestop 2>/dev/null || true
