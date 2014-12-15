#!/usr/bin/env python2.7

import os
import sys
import platform

arch = platform.machine()
python_major = sys.version_info.major
python_minor = sys.version_info.minor
python = "python%d.%d" % (python_major, python_minor)

SICKRAGE_PATH = "/usr/pbi/sickrage-%s" % arch
SICKRAGE_UI = os.path.join(SICKRAGE_PATH, "sickrageUI")
PYTHON_SITE_PACKAGES = os.path.join(SICKRAGE_PATH,
    "lib/%s/site-packages" % python)

sys.path.append(PYTHON_SITE_PACKAGES)
sys.path.append(SICKRAGE_PATH)
sys.path.append(SICKRAGE_UI)

os.environ["DJANGO_SETTINGS_MODULE"] = "sickrageUI.settings"

from django.core.management import execute_from_command_line

if __name__ == "__main__":
    execute_from_command_line(sys.argv)
