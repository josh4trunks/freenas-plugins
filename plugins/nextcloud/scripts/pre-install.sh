#!/bin/sh
#########################################

nextcloud_pbi_path=/usr/pbi/nextcloud-$(uname -m)

# Backup Nextcloud config
if [ -f "${nextcloud_pbi_path}/www/nextcloud/config/config.php" ]; then
	mv ${nextcloud_pbi_path}/www/nextcloud/config/config.php /media
fi
