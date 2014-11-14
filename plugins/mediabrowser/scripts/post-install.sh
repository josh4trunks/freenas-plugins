#!/bin/sh

mediabrowser_pbi_path=/usr/pbi/mediabrowser-$(uname -m)

${mediabrowser_pbi_path}/bin/python2.7 ${mediabrowser_pbi_path}/mediabrowserUI/manage.py syncdb --migrate --noinput