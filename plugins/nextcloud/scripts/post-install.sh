#!/bin/sh
#########################################

nextcloud_pbi_path=/usr/pbi/nextcloud-$(uname -m)

${nextcloud_pbi_path}/bin/python2.7 ${nextcloud_pbi_path}/nextcloudUI/manage.py syncdb --migrate --noinput

# Create Apache alias for Nextcloud
cat << __EOF__ > ${nextcloud_pbi_path}/etc/apache24/Includes/nextcloud.conf
AddType application/x-httpd-php .php

Alias / ${nextcloud_pbi_path}/www/nextcloud/
<Directory ${nextcloud_pbi_path}/www/nextcloud>
    AllowOverride All
    Require all granted
</Directory>
__EOF__

# Add paths to Apache
cat << __EOF__ > ${nextcloud_pbi_path}/etc/apache24/envvars.d/path.env
export PATH=${nextcloud_pbi_path}/bin:/usr/local/bin:\$PATH
export LD_LIBRARY_PATH=/usr/local/lib:\$LD_LIBRARY_PATH
__EOF__

# Optimize Apache on ZFS
sed -i '' -e 's/^#\(EnableMMAP[[:space:]]\).*$/\1Off/' ${nextcloud_pbi_path}/etc/apache24/httpd.conf

# Enable "Pretty URLs"
sed -i '' -e 's/^#\(LoadModule[[:space:]]*rewrite_module[[:space:]].*$\)/\1/' ${nextcloud_pbi_path}/etc/apache24/httpd.conf

# Enable SSL
sed -i '' -e 's|^#\(Include[[:space:]].*/httpd-ssl.conf$\)|\1|' ${nextcloud_pbi_path}/etc/apache24/httpd.conf
sed -i '' -e 's/^#\(LoadModule[[:space:]]*ssl_module[[:space:]].*$\)/\1/' ${nextcloud_pbi_path}/etc/apache24/httpd.conf
sed -i '' -e 's/^#\(LoadModule[[:space:]]*socache_shmcb_module[[:space:]].*$\)/\1/' ${nextcloud_pbi_path}/etc/apache24/httpd.conf

# Make sure SSL config exists
if [ ! -f "${nextcloud_pbi_path}/openssl/openssl.cnf" ]; then
        ln -s openssl.cnf.sample ${nextcloud_pbi_path}/openssl/openssl.cnf
fi

tmp=$(mktemp /tmp/tmp.XXXXXX)
# Generate SSL certificate
if [ ! -f "${nextcloud_pbi_path}/etc/apache24/server.crt" ]; then

	if ! grep -e '^commonName_default[[:space:]]*=' /etc/ssl/openssl.cnf; then
		sed -i '' -e '/^commonName_max[[:space:]]*=/ a\
commonName_default = Nextcloud\
' /etc/ssl/openssl.cnf
	fi
	dd if=/dev/urandom count=16 bs=1 2> /dev/null | uuencode -|head -2 |tail -1 > "${tmp}"
	openssl req -batch -passout file:"${tmp}" -new -x509 -keyout ${nextcloud_pbi_path}/etc/apache24/server.key.out -out ${nextcloud_pbi_path}/etc/apache24/server.crt
	openssl rsa -passin file:"${tmp}" -in ${nextcloud_pbi_path}/etc/apache24/server.key.out -out ${nextcloud_pbi_path}/etc/apache24/server.key

fi

# Create PHP configuration file
if [ ! -f "${nextcloud_pbi_path}/etc/php.ini" ]; then
	cat << __EOF__ > ${nextcloud_pbi_path}/etc/php.ini
[PHP]
apc.enable_cli=1
__EOF__
fi

# Create MySQL server configuration file
if [ ! -f "${nextcloud_pbi_path}/etc/my.cnf" ]; then
	cat << __EOF__ > ${nextcloud_pbi_path}/etc/my.cnf
[server]
skip-networking
skip-name-resolve
expire_logs_days = 1
innodb_flush_method = O_DIRECT
skip-innodb_doublewrite
innodb_flush_log_at_trx_commit = 2
innodb_file_per_table
__EOF__
fi

sysrc 'mysql_enable=YES'
service mysql-server start

# Restore Nextcloud config otherwise set /media as the Nextcloud data-directory
if [ -f "/media/config.php" ]; then
        mv /media/config.php ${nextcloud_pbi_path}/www/nextcloud/config
else
        cat << __EOF__ > ${nextcloud_pbi_path}/www/nextcloud/config/autoconfig.php
<?php
\$AUTOCONFIG = array (
  'dbtype' => 'mysql',
  'dbname' => 'nextcloud',
  'dbuser' => 'ncuser',
  'dbpass' => 'ncpass',
  'dbhost' => 'localhost:/tmp/mysql.sock',
  'directory' => '/media',
);
__EOF__
        cat << __EOF__ > ${nextcloud_pbi_path}/www/nextcloud/config/config.php
<?php
\$CONFIG = array (
  'memcache.local' => '\OC\Memcache\APCu',
  'htaccess.RewriteBase' => '/',
);
__EOF__

	${nextcloud_pbi_path}/bin/mysql -e "CREATE DATABASE nextcloud;"
	${nextcloud_pbi_path}/bin/mysql -e "GRANT ALL PRIVILEGES ON nextcloud.* TO 'ncuser'@'localhost' IDENTIFIED BY 'ncpass';"
	${nextcloud_pbi_path}/bin/mysql -e "FLUSH PRIVILEGES;"
fi

# Allow Nextcloud updater to work
chown -R www:www ${nextcloud_pbi_path}/www/nextcloud /media
chmod -R u+w ${nextcloud_pbi_path}/www/nextcloud

# Create cronjob for Nextcloud
echo "*/15 * * * * ${nextcloud_pbi_path}/bin/php -f ${nextcloud_pbi_path}/www/nextcloud/cron.php" > ${tmp}
crontab -u www ${tmp}
