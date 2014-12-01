#!/bin/sh
#########################################

transmission_pbi_path=/usr/pbi/transmission-$(uname -m)

${transmission_pbi_path}/etc/rc.d/transmission forcestop 2>/dev/null || true
