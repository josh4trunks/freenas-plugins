#!/bin/sh
#########################################

maraschino_pbi_path=/usr/pbi/maraschino-$(uname -m)

${maraschino_pbi_path}/bin/python2.7 ${maraschino_pbi_path}/maraschinoUI/manage.py syncdb --migrate --noinput

# Temporary workaround for a valid certificate store
ln -s /usr/local/share/certs/ca-root-nss.crt /etc/ssl/cert.pem
mkdir -p /usr/local/openssl
ln -s /usr/local/share/certs/ca-root-nss.crt /usr/local/openssl/cert.pem
