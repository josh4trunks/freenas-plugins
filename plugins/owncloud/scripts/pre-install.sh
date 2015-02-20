#!/bin/sh
#########################################

owncloud_pbi_path=/usr/pbi/owncloud-$(uname -m)

# Backup ownCloud config
if [ -f "${owncloud_pbi_path}/www/owncloud/config/config.php" ]; then
	mv ${owncloud_pbi_path}/www/owncloud/config/config.php /media
fi
