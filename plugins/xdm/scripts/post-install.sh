#!/bin/sh

xdm_pbi_path=/usr/pbi/xdm-$(uname -m)

${xdm_pbi_path}/bin/python ${xdm_pbi_path}/xdmUI/manage.py syncdb --migrate --noinput
