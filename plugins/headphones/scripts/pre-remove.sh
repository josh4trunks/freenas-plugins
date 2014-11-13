#!/bin/sh

headphones_pbi_path=/usr/pbi/headphones-$(uname -m)

${headphones_pbi_path}/etc/rc.d/headphones forcestop 2>/dev/null || true
