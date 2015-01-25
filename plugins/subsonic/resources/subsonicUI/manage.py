#!/usr/bin/env python2.7

import os
import sys
import platform

arch = platform.machine()
python_major = sys.version_info.major
python_minor = sys.version_info.minor
python = "python%d.%d" % (python_major, python_minor)

SUBSONIC_PATH = "/usr/pbi/subsonic-%s" % arch
SUBSONIC_UI = os.path.join(SUBSONIC_PATH, "subsonicUI")
PYTHON_SITE_PACKAGES = os.path.join(SUBSONIC_PATH,
    "lib/%s/site-packages" % python)

sys.path.append(PYTHON_SITE_PACKAGES)
sys.path.append(SUBSONIC_PATH)
sys.path.append(SUBSONIC_UI)

os.environ["DJANGO_SETTINGS_MODULE"] = "subsonicUI.settings"

from django.core.management import execute_from_command_line

if __name__ == "__main__":
    execute_from_command_line(sys.argv)
