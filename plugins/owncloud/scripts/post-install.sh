#!/bin/sh
#########################################

owncloud_pbi_path=/usr/pbi/owncloud-$(uname -m)

${owncloud_pbi_path}/bin/python2.7 ${owncloud_pbi_path}/owncloudUI/manage.py syncdb --migrate --noinput

# Create Apache alias for ownCloud
cat << __EOF__ > ${owncloud_pbi_path}/etc/apache24/Includes/owncloud.conf
AddType application/x-httpd-php .php

Alias / ${owncloud_pbi_path}/www/owncloud/
<Directory ${owncloud_pbi_path}/www/owncloud>
    AllowOverride All
    Require all granted
</Directory>
__EOF__

# Add paths to Apache
cat << __EOF__ > ${owncloud_pbi_path}/etc/apache24/envvars.d/path.env
export PATH=${owncloud_pbi_path}/bin:/usr/local/bin:\$PATH
export LD_LIBRARY_PATH=/usr/local/lib:\$LD_LIBRARY_PATH
__EOF__

# Optimize Apache on ZFS
sed -i '' -e 's/^#\(EnableMMAP[[:space:]]\).*$/\1Off/' ${owncloud_pbi_path}/etc/apache24/httpd.conf

# Enable "Pretty URLs"
sed -i '' -e 's/^#\(LoadModule[[:space:]]*rewrite_module[[:space:]].*$\)/\1/' ${owncloud_pbi_path}/etc/apache24/httpd.conf

# Enable SSL
sed -i '' -e 's|^#\(Include[[:space:]].*/httpd-ssl.conf$\)|\1|' ${owncloud_pbi_path}/etc/apache24/httpd.conf
sed -i '' -e 's/^#\(LoadModule[[:space:]]*ssl_module[[:space:]].*$\)/\1/' ${owncloud_pbi_path}/etc/apache24/httpd.conf
sed -i '' -e 's/^#\(LoadModule[[:space:]]*socache_shmcb_module[[:space:]].*$\)/\1/' ${owncloud_pbi_path}/etc/apache24/httpd.conf

# Make sure SSL config exists
if [ ! -f "${owncloud_pbi_path}/openssl/openssl.cnf" ]; then
        ln -s openssl.cnf.sample ${owncloud_pbi_path}/openssl/openssl.cnf
fi

tmp=$(mktemp /tmp/tmp.XXXXXX)
# Generate SSL certificate
if [ ! -f "${owncloud_pbi_path}/etc/apache24/server.crt" ]; then

	if ! grep -e '^commonName_default[[:space:]]*=' /etc/ssl/openssl.cnf; then
		sed -i '' -e '/^commonName_max[[:space:]]*=/ a\
commonName_default = ownCloud\
' /etc/ssl/openssl.cnf
	fi
	dd if=/dev/urandom count=16 bs=1 2> /dev/null | uuencode -|head -2 |tail -1 > "${tmp}"
	openssl req -batch -passout file:"${tmp}" -new -x509 -keyout ${owncloud_pbi_path}/etc/apache24/server.key.out -out ${owncloud_pbi_path}/etc/apache24/server.crt
	openssl rsa -passin file:"${tmp}" -in ${owncloud_pbi_path}/etc/apache24/server.key.out -out ${owncloud_pbi_path}/etc/apache24/server.key

fi

# Create PHP configuration file
if [ ! -f "${owncloud_pbi_path}/etc/php.ini" ]; then
	cat << __EOF__ > ${owncloud_pbi_path}/etc/php.ini
[PHP]
apc.enable_cli=1
__EOF__
fi

# Restore ownCloud config otherwise set /media as the ownCloud data-directory
if [ -f "/media/config.php" ]; then
        mv /media/config.php ${owncloud_pbi_path}/www/owncloud/config
else
        cat << __EOF__ > ${owncloud_pbi_path}/www/owncloud/config/autoconfig.php
<?php
\$AUTOCONFIG = array (
  'dbtype' => 'sqlite',
  'directory' => '/media',
);
__EOF__
        cat << __EOF__ > ${owncloud_pbi_path}/www/owncloud/config/config.php
<?php
\$CONFIG = array (
  'memcache.local' => '\OC\Memcache\APCu',
  'htaccess.RewriteBase' => '/',
);
__EOF__
fi

# Allow ownCloud updater to work
chown -R www:www ${owncloud_pbi_path}/www/owncloud /media
chmod -R u+w ${owncloud_pbi_path}/www/owncloud

# Create cronjob for ownCloud
echo "*/15 * * * * ${owncloud_pbi_path}/bin/php -f ${owncloud_pbi_path}/www/owncloud/cron.php" > ${tmp}
crontab -u www ${tmp}
