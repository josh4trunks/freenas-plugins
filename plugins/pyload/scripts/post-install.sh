#!/bin/sh
#########################################

pyload_pbi_path=/usr/pbi/pyload-$(uname -m)

${pyload_pbi_path}/bin/python2.7 ${pyload_pbi_path}/pyloadUI/manage.py syncdb --migrate --noinput
