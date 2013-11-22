#!/bin/sh

headphones_pbi_path=/usr/pbi/headphones-$(uname -m)

${headphones_pbi_path}/bin/python ${headphones_pbi_path}/headphonesUI/manage.py syncdb --migrate --noinput
