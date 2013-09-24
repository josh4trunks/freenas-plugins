#!/bin/sh
#########################################

crashplan_pbi_path=/usr/pbi/crashplan-$(uname -m)

${crashplan_pbi_path}/bin/python ${crashplan_pbi_path}/crashplanUI/manage.py syncdb --migrate --noinput
