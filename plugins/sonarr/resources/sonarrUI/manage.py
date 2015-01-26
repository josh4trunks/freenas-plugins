#!/usr/bin/env python2.7

import os
import sys
import platform

arch = platform.machine()
python_major = sys.version_info.major
python_minor = sys.version_info.minor
python = "python%d.%d" % (python_major, python_minor)

SONARR_PATH = "/usr/pbi/sonarr-%s" % arch
SONARR_UI = os.path.join(SONARR_PATH, "sonarrUI")
PYTHON_SITE_PACKAGES = os.path.join(SONARR_PATH,
    "lib/%s/site-packages" % python)

sys.path.append(PYTHON_SITE_PACKAGES)
sys.path.append(SONARR_PATH)
sys.path.append(SONARR_UI)

os.environ["DJANGO_SETTINGS_MODULE"] = "sonarrUI.settings"

from django.core.management import execute_from_command_line

if __name__ == "__main__":
    execute_from_command_line(sys.argv)
