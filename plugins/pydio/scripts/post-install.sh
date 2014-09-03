#!/bin/sh
#########################################

pydio_pbi_path=/usr/pbi/pydio-$(uname -m)/

/bin/cp ${pydio_pbi_path}/etc/rc.d/apache24 /usr/local/etc/rc.d/

${pydio_pbi_path}/bin/python2.7 ${pydio_pbi_path}/pydioUI/manage.py syncdb --migrate --noinput


# Generate pydio.conf file for apache
cat << __EOF__ > ${pydio_pbi_path}/etc/apache24/Includes/pydio.conf
Listen 80
<VirtualHost *:80>
  DirectoryIndex index.html index.php
  alias /gui ${pydio_pbi_path}/www/pydio
  <Directory ${pydio_pbi_path}/www/pydio>
        Options FollowSymLinks
        AllowOverride All
        Order allow,deny
        Allow from all
  </Directory>

  <Directory />
        Options FollowSymLinks
        AllowOverride All
        Order allow,deny
        allow from all
  </Directory>

</VirtualHost>

__EOF__

cat << __EOF__ > ${pydio_pbi_path}/etc/apache24/httpd.conf
# Generating apache general httpd.conf
# The absolutely necessary modules
LoadModule authn_file_module libexec/apache24/mod_authn_file.so
LoadModule authn_core_module libexec/apache24/mod_authn_core.so
LoadModule authz_user_module libexec/apache24/mod_authz_user.so
LoadModule authz_core_module libexec/apache24/mod_authz_core.so
LoadModule alias_module libexec/apache24/mod_alias.so
LoadModule mpm_itk_module libexec/apache24/mod_mpm_itk.so
LoadModule unixd_module libexec/apache24/mod_unixd.so
LoadModule auth_basic_module libexec/apache24/mod_auth_basic.so
LoadModule auth_digest_module libexec/apache24/mod_auth_digest.so
LoadModule setenvif_module libexec/apache24/mod_setenvif.so
LoadModule dav_module libexec/apache24/mod_dav.so
LoadModule dav_fs_module libexec/apache24/mod_dav_fs.so
LoadModule allowmethods_module libexec/apache24/mod_allowmethods.so
LoadModule ssl_module libexec/apache24/mod_ssl.so
LoadModule socache_shmcb_module libexec/apache24/mod_socache_shmcb.so

# The modules neede for pydio
LoadModule rewrite_module libexec/apache24/mod_rewrite.so
LoadModule php5_module libexec/apache/libphp5.so

# The still deciding whether or not to keep thse modules or not
LoadModule authz_host_module libexec/apache24/mod_authz_host.so
LoadModule authz_groupfile_module libexec/apache24/mod_authz_groupfile.so
LoadModule access_compat_module libexec/apache24/mod_access_compat.so
LoadModule reqtimeout_module libexec/apache24/mod_reqtimeout.so
LoadModule filter_module libexec/apache24/mod_filter.so
LoadModule mime_module libexec/apache24/mod_mime.so
LoadModule log_config_module libexec/apache24/mod_log_config.so
LoadModule env_module libexec/apache24/mod_env.so
LoadModule headers_module libexec/apache24/mod_headers.so
#LoadModule version_module libexec/apache24/mod_version.so
LoadModule status_module libexec/apache24/mod_status.so
LoadModule autoindex_module libexec/apache24/mod_autoindex.so
LoadModule dir_module libexec/apache24/mod_dir.so

# Third party modules
IncludeOptional etc/apache24/modules.d/[0-9][0-9][0-9]_*.conf
 
<IfModule unixd_module>
User www
Group www
</IfModule>

<IfModule dir_module>
    DirectoryIndex index.html
</IfModule>

<Files ".ht*">
    Require all denied
</Files>

ErrorLog "/var/log/httpd-error.log"
LogLevel warn

<IfModule log_config_module>
    LogFormat "%h %l %u %t \"%r\" %>s %b \"%{Referer}i\" \"%{User-Agent}i\"" combined
    LogFormat "%h %l %u %t \"%r\" %>s %b" common
    <IfModule logio_module>
      LogFormat "%h %l %u %t \"%r\" %>s %b \"%{Referer}i\" \"%{User-Agent}i\" %I %O" combinedio
    </IfModule>
    CustomLog "/var/log/httpd-access.log" common

</IfModule>

<IfModule alias_module>
    ScriptAlias /cgi-bin/ "/usr/local/www/apache24/cgi-bin/"
</IfModule>

<IfModule mime_module>
    #
    # TypesConfig points to the file containing the list of mappings from
    # filename extension to MIME-type.
    #
    TypesConfig etc/apache24/mime.types

    #
    # AddType allows you to add to or override the MIME configuration
    # file specified in TypesConfig for specific file types.
    #
    #AddType application/x-gzip .tgz
    #
    # AddEncoding allows you to have certain browsers uncompress
    # information on the fly. Note: Not all browsers support this.
    #
    #AddEncoding x-compress .Z
    #AddEncoding x-gzip .gz .tgz
    #
    # If the AddEncoding directives above are commented-out, then you
    # probably should define those extensions to indicate media types:
    #
    AddType application/x-compress .Z
    AddType application/x-gzip .gz .tgz

    #
    # AddHandler allows you to map certain file extensions to "handlers":
    # actions unrelated to filetype. These can be either built into the server
    # or added with the Action directive (see below)
    #
    # To use CGI scripts outside of ScriptAliased directories:
    # (You will also need to add "ExecCGI" to the "Options" directive.)
    #
    #AddHandler cgi-script .cgi

    # For type maps (negotiated resources):
    #AddHandler type-map var

    #
    # Filters allow you to process content before it is sent to the client.
    #
    # To parse .shtml files for server-side includes (SSI):
    # (You will also need to add "Includes" to the "Options" directive.)
    #
    #AddType text/html .shtml
    #AddOutputFilter INCLUDES .shtml
</IfModule>

# Secure (SSL/TLS) connections
#Include etc/apache24/extra/httpd-ssl.conf
#
# Note: The following must must be present to support
#       starting without SSL on platforms with no /dev/random equivalent
#       but a statically compiled-in mod_ssl.
#
<IfModule ssl_module>
SSLRandomSeed startup builtin
SSLRandomSeed connect builtin
</IfModule>

# addition to enable mod_php5
<FilesMatch "\.php$">
    SetHandler application/x-httpd-php
</FilesMatch>
<FilesMatch "\.phps$">
    SetHandler application/x-httpd-php-source
</FilesMatch>


Include etc/apache24/Includes/*.conf

__EOF__


# Generate php.ini file

cat << __EOF__ > ${pydio_pbi_path}/etc/php.ini

[PHP]

;;;;;;;;;;;;;;;;;;;;
; Language Options ;
;;;;;;;;;;;;;;;;;;;;
engine = On

short_open_tag = Off

asp_tags = Off
precision = 14
output_buffering = Off

zlib.output_compression = Off
implicit_flush = Off

unserialize_callback_func =
serialize_precision = 17
disable_functions =
disable_classes =


zend.enable_gc = On

;;;;;;;;;;;;;;;;;
; Miscellaneous ;
;;;;;;;;;;;;;;;;;

expose_php = On

;;;;;;;;;;;;;;;;;;;
; Resource Limits ;
;;;;;;;;;;;;;;;;;;;
max_execution_time = 30
max_input_time = 60

memory_limit = 128M

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
; Error handling and logging ;
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
error_reporting = E_ALL
display_errors = On
display_startup_errors = On
log_errors = On
log_errors_max_len = 1024
ignore_repeated_errors = Off
ignore_repeated_source = Off
report_memleaks = On

track_errors = On
html_errors = On

;;;;;;;;;;;;;;;;;
; Data Handling ;
;;;;;;;;;;;;;;;;;
variables_order = "GPCS"
request_order = "GP"

register_argc_argv = Off
auto_globals_jit = On
post_max_size = 8M
auto_prepend_file =
auto_append_file =
default_mimetype = "text/html"

;;;;;;;;;;;;;;;;;;;;;;;;;
; Paths and Directories ;
;;;;;;;;;;;;;;;;;;;;;;;;;
doc_root =
user_dir =
enable_dl = Off


;;;;;;;;;;;;;;;;
; File Uploads ;
;;;;;;;;;;;;;;;;

file_uploads = On

upload_max_filesize = 2M
max_file_uploads = 20

;;;;;;;;;;;;;;;;;;
; Fopen wrappers ;
;;;;;;;;;;;;;;;;;;
allow_url_fopen = On
allow_url_include = Off
default_socket_timeout = 60

;;;;;;;;;;;;;;;;;;;
; Module Settings ;
;;;;;;;;;;;;;;;;;;;

[CLI Server]
cli_server.color = On

[Pdo_mysql]
pdo_mysql.cache_size = 2000
pdo_mysql.default_socket=

[mail function]
SMTP = localhost
smtp_port = 25
mail.add_x_header = On

[SQL]
sql.safe_mode = Off

[ODBC]
odbc.allow_persistent = On
odbc.check_persistent = On
odbc.max_persistent = -1
odbc.max_links = -1
odbc.defaultlrl = 4096
odbc.defaultbinmode = 1

;birdstep.max_links = -1

[Interbase]
ibase.allow_persistent = 1

ibase.max_persistent = -1

ibase.max_links = -1

ibase.timestampformat = "%Y-%m-%d %H:%M:%S"

ibase.dateformat = "%Y-%m-%d"

ibase.timeformat = "%H:%M:%S"

[MySQL]
mysql.allow_local_infile = On

mysql.allow_persistent = On
mysql.cache_size = 2000
mysql.max_persistent = -1

mysql.max_links = -1
mysql.default_port =
mysql.default_socket =
mysql.default_host =
mysql.default_user =
mysql.default_password =
mysql.connect_timeout = 60
mysql.trace_mode = Off

[MySQLi]
mysqli.max_persistent = -1
mysqli.allow_persistent = On
mysqli.max_links = -1
mysqli.cache_size = 2000

mysqli.default_port = 3306

mysqli.default_socket =

mysqli.default_host =
mysqli.default_user =
mysqli.default_pw =
mysqli.reconnect = Off

[mysqlnd]
mysqlnd.collect_statistics = On
mysqlnd.collect_memory_statistics = On


[Sybase-CT]
sybct.allow_persistent = On
sybct.max_persistent = -1
sybct.max_links = -1
sybct.min_server_severity = 10
sybct.min_client_severity = 10

[bcmath]
bcmath.scale = 0

[Session]
session.save_path = "/tmp"
session.use_cookies = 1
session.use_only_cookies = 1
session.name = PHPSESSID
session.auto_start = 0
session.cookie_lifetime = 0
session.cookie_path = /
session.cookie_domain =
session.cookie_httponly =
session.serialize_handler = php
session.gc_probability = 1
session.gc_divisor = 1000
session.gc_maxlifetime = 1440
session.referer_check =

session.cache_limiter = nocache
session.cache_expire = 180

http://php.net/session.use-trans-sid
session.use_trans_sid = 0
session.hash_function = 0

session.hash_bits_per_character = 5

url_rewriter.tags = "a=href,area=href,frame=src,input=src,form=fakeentry"


[MSSQL]
; Allow or prevent persistent links.
mssql.allow_persistent = On

; Maximum number of persistent links.  -1 means no limit.
mssql.max_persistent = -1

; Maximum number of links (persistent+non persistent).  -1 means no limit.
mssql.max_links = -1

; Minimum error severity to display.
mssql.min_error_severity = 10

; Minimum message severity to display.
mssql.min_message_severity = 10

; Compatibility mode with old versions of PHP 3.0.
mssql.compatability_mode = Off

; Use NT authentication when connecting to the server
mssql.secure_connection = Off

[Tidy]
tidy.clean_output = Off

[soap]
soap.wsdl_cache_enabled=1
soap.wsdl_cache_dir="/tmp"

soap.wsdl_cache_ttl=86400

; Sets the size of the cache limit. (Max. number of WSDL files to cache)
soap.wsdl_cache_limit = 5

[ldap]
; Sets the maximum number of open links or -1 for unlimited.
ldap.max_links = -1
__EOF__

# Generate SSL certificate
if [ ! -f "${pydio_pbi_path}/etc/apache24/server.crt" ]; then

	if ! fgrep "commonName_default" /etc/ssl/openssl.cnf; then
		/usr/bin/sed -i '' -E 's/(^commonName_max.*)/\1\
commonName_default = pydio/' /etc/ssl/openssl.cnf
	fi
	tmp=$(mktemp /tmp/tmp.XXXXXX)
	dd if=/dev/urandom count=16 bs=1 2> /dev/null | uuencode -|head -2 |tail -1 > "${tmp}"
	/usr/bin/openssl req -batch -passout file:"${tmp}" -new -x509 -keyout ${pydio_pbi_path}/etc/apache24/server.key.out -out ${pydio_pbi_path}/etc/apache24/server.crt
	/usr/bin/openssl rsa -passin file:"${tmp}" -in ${pydio_pbi_path}/etc/apache24/server.key.out -out ${pydio_pbi_path}/etc/apache24/server.key

fi

#Enable SSL
/usr/bin/sed -i '' -E -e 's/^#(.*httpd-ssl.conf)/\1/' ${pydio_pbi_path}/etc/apache24/httpd.conf