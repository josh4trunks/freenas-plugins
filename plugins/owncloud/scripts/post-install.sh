#!/bin/sh
#########################################

owncloud_pbi_path=/usr/pbi/owncloud-$(uname -m)

/bin/cp ${owncloud_pbi_path}/etc/rc.d/apache22 /usr/local/etc/rc.d/

${owncloud_pbi_path}/bin/python ${owncloud_pbi_path}/owncloudUI/manage.py syncdb --migrate --noinput

chown www:www ${owncloud_pbi_path}/www/owncloud \
	${owncloud_pbi_path}/www/owncloud/apps \
	${owncloud_pbi_path}/www/owncloud/config

cat << __EOF__ > ${owncloud_pbi_path}/etc/apache22/Includes/owncloud.conf
Alias / ${owncloud_pbi_path}/www/owncloud/
AcceptPathInfo On
<Directory ${owncloud_pbi_path}/www/owncloud>
    AllowOverride All
    Order Allow,Deny
    Allow from all
</Directory>
__EOF__
