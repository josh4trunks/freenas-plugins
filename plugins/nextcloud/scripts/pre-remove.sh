#!/bin/sh
#########################################

nextcloud_pbi_path=/usr/pbi/nextcloud-$(uname -m)

${nextcloud_pbi_path}/etc/rc.d/mysql-server forcestop 2>/dev/null || true
${nextcloud_pbi_path}/etc/rc.d/apache24 forcestop 2>/dev/null || true
