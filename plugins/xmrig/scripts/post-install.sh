#!/bin/sh
#########################################

xmrig_pbi_path=/usr/pbi/xmrig-$(uname -m)

${xmrig_pbi_path}/bin/python2.7 ${xmrig_pbi_path}/xmrigUI/manage.py syncdb --migrate --noinput
