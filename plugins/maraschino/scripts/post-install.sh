#!/bin/sh

maraschino_pbi_path=/usr/pbi/maraschino-$(uname -m)

${maraschino_pbi_path}/bin/python ${maraschino_pbi_path}/maraschinoUI/manage.py syncdb --migrate --noinput
