#!/bin/sh

btsync_pbi_path=/usr/pbi/btsync-$(uname -m)

${btsync_pbi_path}/bin/python ${btsync_pbi_path}/btsyncUI/manage.py syncdb --migrate --noinput
