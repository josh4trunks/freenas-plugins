#!/bin/sh

subsonic_pbi_path=/usr/pbi/subsonic-$(uname -m)

${subsonic_pbi_path}/bin/python ${subsonic_pbi_path}/subsonicUI/manage.py syncdb --migrate --noinput
