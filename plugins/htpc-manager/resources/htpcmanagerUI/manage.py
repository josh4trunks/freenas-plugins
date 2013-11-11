#!/usr/bin/env python

import os
import sys
import platform

arch = platform.machine()
python_major = sys.version_info.major
python_minor = sys.version_info.minor
python = "python%d.%d" % (python_major, python_minor)

HTPCMANAGER_PATH = "/usr/pbi/htpc-manager-%s" % arch
HTPCMANAGER_UI = os.path.join(HTPCMANAGER_PATH, "htpcmanagerUI")
PYTHON_SITE_PACKAGES = os.path.join(HTPCMANAGER_PATH,"lib/%s/site-packages" % python)

sys.path.append(PYTHON_SITE_PACKAGES)
sys.path.append(HTPCMANAGER_PATH)
sys.path.append(HTPCMANAGER_UI)

os.environ["DJANGO_SETTINGS_MODULE"] = "htpcmanagerUI.settings"

from django.core.management import execute_from_command_line

if __name__ == "__main__":
    execute_from_command_line(sys.argv)
