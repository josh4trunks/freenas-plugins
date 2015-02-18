#!/bin/sh
#########################################

owncloud_pbi_path=/usr/pbi/owncloud-$(uname -m)

${owncloud_pbi_path}/bin/python2.7 ${owncloud_pbi_path}/owncloudUI/manage.py syncdb --migrate --noinput

if [ ! -f "${owncloud_pbi_path}/www/owncloud/config/config.php" ]; then
	cat << __EOF__ > ${owncloud_pbi_path}/www/owncloud/config/config.php
	<?php
	\$CONFIG = array (
	  'datadirectory' => '/media',
	);
	?>
__EOF__
fi

cat << __EOF__ > ${owncloud_pbi_path}/etc/apache24/Includes/owncloud.conf
AddType application/x-httpd-php .php

Alias / ${owncloud_pbi_path}/www/owncloud/
AcceptPathInfo On
<Directory ${owncloud_pbi_path}/www/owncloud>
    Options Indexes FollowSymLinks
    AllowOverride All
    Require all granted
    SetEnv MOD_X_SENDFILE_ENABLED 1
    XSendFile On
    XSendFilePath /media
</Directory>
__EOF__

chown -R www:www ${owncloud_pbi_path}/www/owncloud \
	/media


# Generate SSL certificate
if [ ! -f "${owncloud_pbi_path}/etc/apache22/server.crt" ]; then

	if ! fgrep "commonName_default" /etc/ssl/openssl.cnf; then
		/usr/bin/sed -i '' -E 's/(^commonName_max.*)/\1\
commonName_default = ownCloud/' /etc/ssl/openssl.cnf
	fi
	tmp=$(mktemp /tmp/tmp.XXXXXX)
	dd if=/dev/urandom count=16 bs=1 2> /dev/null | uuencode -|head -2 |tail -1 > "${tmp}"
	/usr/bin/openssl req -batch -passout file:"${tmp}" -new -x509 -keyout ${owncloud_pbi_path}/etc/apache22/server.key.out -out ${owncloud_pbi_path}/etc/apache22/server.crt
	/usr/bin/openssl rsa -passin file:"${tmp}" -in ${owncloud_pbi_path}/etc/apache22/server.key.out -out ${owncloud_pbi_path}/etc/apache22/server.key

fi

#Enable SSL
/usr/bin/sed -i '' -e 's|^#\(Include[[:space:]].*/httpd-ssl.conf$\)|\1/' ${owncloud_pbi_path}/etc/apache22/httpd.conf

#Optimize Apache on ZFS
/usr/bin/sed -i '' -e 's/^#\(EnableMMAP[[:space:]].*$\)/\1Off/' ${owncloud_pbi_path}/etc/apache24/httpd.conf

#Enable X-Sendfile
/usr/bin/sed -i '' -e 's/^#\(LoadModule[[:space:]]*xsendfile_module[[:space:]].*$\)/\1/' ${owncloud_pbi_path}/etc/apache24/httpd.conf
