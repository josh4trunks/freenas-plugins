#!/usr/bin/env python2.7

import os
import sys
import platform

arch = platform.machine()
python_major = sys.version_info.major
python_minor = sys.version_info.minor
python = "python%d.%d" % (python_major, python_minor)

BTSYNC_PATH = "/usr/pbi/btsync-%s" % arch
BTSYNC_UI = os.path.join(BTSYNC_PATH, "btsyncUI")
PYTHON_SITE_PACKAGES = os.path.join(BTSYNC_PATH,"lib/%s/site-packages" % python)

sys.path.append(PYTHON_SITE_PACKAGES)
sys.path.append(BTSYNC_PATH)
sys.path.append(BTSYNC_UI)

os.environ["DJANGO_SETTINGS_MODULE"] = "btsyncUI.settings"

from django.core.management import execute_from_command_line

if __name__ == "__main__":
    execute_from_command_line(sys.argv)
