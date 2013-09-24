#!/usr/bin/env python

import os
import sys
import platform

arch = platform.machine()
python_major = sys.version_info.major
python_minor = sys.version_info.minor
python = "python%d.%d" % (python_major, python_minor)

OWNCLOUD_PATH = "/usr/pbi/owncloud-%s" % arch
OWNCLOUD_UI = os.path.join(OWNCLOUD_PATH, "owncloudUI")
PYTHON_SITE_PACKAGES = os.path.join(OWNCLOUD_PATH,
    "lib/%s/site-packages" % python)

sys.path.append(PYTHON_SITE_PACKAGES)
sys.path.append(OWNCLOUD_PATH)
sys.path.append(OWNCLOUD_UI)

os.environ["DJANGO_SETTINGS_MODULE"] = "owncloudUI.settings"

from django.core.management import execute_from_command_line

if __name__ == "__main__":
    execute_from_command_line(sys.argv)
