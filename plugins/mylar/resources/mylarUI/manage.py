#!/usr/bin/env python

import os
import sys
import platform

arch = platform.machine()
python_major = sys.version_info.major
python_minor = sys.version_info.minor
python = "python%d.%d" % (python_major, python_minor)

MYLAR_PATH = "/usr/pbi/mylar-%s" % arch
MYLAR_UI = os.path.join(MYLAR_PATH, "mylarUI")
PYTHON_SITE_PACKAGES = os.path.join(MYLAR_PATH,"lib/%s/site-packages" % python)

sys.path.append(PYTHON_SITE_PACKAGES)
sys.path.append(MYLAR_PATH)
sys.path.append(MYLAR_UI)

os.environ["DJANGO_SETTINGS_MODULE"] = "mylarUI.settings"

from django.core.management import execute_from_command_line

if __name__ == "__main__":
    execute_from_command_line(sys.argv)
