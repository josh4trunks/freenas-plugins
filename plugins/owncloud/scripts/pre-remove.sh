#!/bin/sh
#########################################

owncloud_pbi_path=/usr/pbi/owncloud-$(uname -m)

${owncloud_pbi_path}/etc/rc.d/apache24 forcestop 2>/dev/null || true
