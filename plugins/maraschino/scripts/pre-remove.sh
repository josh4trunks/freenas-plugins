#!/bin/sh
#########################################

maraschino_pbi_path=/usr/pbi/maraschino-$(uname -m)

${maraschino_pbi_path}/etc/rc.d/maraschino forcestop 2>/dev/null || true
