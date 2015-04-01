#!/bin/sh
#########################################

pyload_pbi_path=/usr/pbi/pyload-$(uname -m)

${pyload_pbi_path}/etc/rc.d/pyload forcestop 2>/dev/null || true
