#!/bin/sh

sickbeard_pbi_path=/usr/pbi/sickbeard-$(uname -m)

${sickbeard_pbi_path}/etc/rc.d/sickbeard forcestop 2>/dev/null || true
