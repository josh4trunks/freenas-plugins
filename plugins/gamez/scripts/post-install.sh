#!/bin/sh

gamez_pbi_path=/usr/pbi/gamez-$(uname -m)

${gamez_pbi_path}/bin/python ${gamez_pbi_path}/gamezUI/manage.py syncdb --migrate --noinput
