#!/bin/sh
#########################################

owncloud_pbi_path=/usr/pbi/owncloud-$(uname -m)

# Backup ownCloud config
mv ${owncloud_pbi_path}/www/owncloud/config/config.php /media
