#!/bin/sh

subsonic_pbi_path=/usr/pbi/subsonic-$(uname -m)

${subsonic_pbi_path}/bin/python2.7 ${subsonic_pbi_path}/subsonicUI/manage.py syncdb --migrate --noinput
