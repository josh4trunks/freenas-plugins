#!/bin/sh
#########################################

nzbhydra_pbi_path=/usr/pbi/nzbhydra-$(uname -m)

${nzbhydra_pbi_path}/bin/python2.7 ${nzbhydra_pbi_path}/nzbhydraUI/manage.py syncdb --migrate --noinput

# Temporary workaround for a valid certificate store
ln -s /usr/local/share/certs/ca-root-nss.crt /etc/ssl/cert.pem
mkdir -p ${nzbhydra_pbi_path}/openssl
ln -s /usr/local/share/certs/ca-root-nss.crt ${nzbhydra_pbi_path}/openssl/cert.pem
