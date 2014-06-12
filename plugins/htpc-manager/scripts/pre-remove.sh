#!/bin/sh

htpc_manager_pbi_path=/usr/pbi/htpc-manager-$(uname -m)

${htpc_manager_pbi_path}/etc/rc.d/htpc-manager forcestop 2>/dev/null || true
