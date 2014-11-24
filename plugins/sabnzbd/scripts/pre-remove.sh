#!/bin/sh
#########################################

sabnzbd_pbi_path=/usr/pbi/sabnzbd-$(uname -m)

${sabnzbd_pbi_path}/etc/rc.d/sabnzbd forcestop 2>/dev/null || true
