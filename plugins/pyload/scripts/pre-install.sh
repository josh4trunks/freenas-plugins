#!/bin/sh
#########################################

pyload_pbi_path=/usr/pbi/pyload-$(uname -m)

if [ ! -d "/var/db/pyload" ]; then
	cp "${pyload_pbi_path}/pyload-setup" "/var/db/pyload"
	chown -R media:media /var/db/pyload
fi
