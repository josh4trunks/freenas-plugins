#!/bin/sh
#########################################

maraschino_pbi_path=/usr/pbi/maraschino-$(uname -m)

${maraschino_pbi_path}/bin/python2.7 ${maraschino_pbi_path}/maraschinoUI/manage.py syncdb --migrate --noinput

# Temporary workaround for a valid certificate store
ln -s /usr/local/share/certs/ca-root-nss.crt /etc/ssl/cert.pem
mkdir -p ${maraschino_pbi_path}/openssl
ln -s /usr/local/share/certs/ca-root-nss.crt ${maraschino_pbi_path}/openssl/cert.pem
