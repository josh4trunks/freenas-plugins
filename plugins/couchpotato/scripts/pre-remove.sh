#!/bin/sh

couchpotato_pbi_path=/usr/pbi/couchpotato-$(uname -m)

${couchpotato_pbi_path}/etc/rc.d/couchpotato forcestop 2>/dev/null || true
