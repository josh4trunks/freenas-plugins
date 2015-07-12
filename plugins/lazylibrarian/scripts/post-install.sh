#!/bin/sh
#########################################

lazylibrarian_pbi_path=/usr/pbi/lazylibrarian-$(uname -m)

${lazylibrarian_pbi_path}/bin/python2.7 ${lazylibrarian_pbi_path}/lazylibrarianUI/manage.py syncdb --migrate --noinput

# Temporary workaround for a valid certificate store
ln -s /usr/local/share/certs/ca-root-nss.crt /etc/ssl/cert.pem
mkdir -p ${lazylibrarian_pbi_path}/openssl
ln -s /usr/local/share/certs/ca-root-nss.crt ${lazylibrarian_pbi_path}/openssl/cert.pem
