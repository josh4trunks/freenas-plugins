#!/usr/bin/env python

import os
import sys
import platform

arch = platform.machine()
python_major = sys.version_info.major
python_minor = sys.version_info.minor
python = "python%d.%d" % (python_major, python_minor)

NEXTCLOUD_PATH = "/usr/pbi/nextcloud-%s" % arch
NEXTCLOUD_UI = os.path.join(NEXTCLOUD_PATH, "nextcloudUI")
PYTHON_SITE_PACKAGES = os.path.join(NEXTCLOUD_PATH,
    "lib/%s/site-packages" % python)

sys.path.append(PYTHON_SITE_PACKAGES)
sys.path.append(NEXTCLOUD_PATH)
sys.path.append(NEXTCLOUD_UI)

os.environ["DJANGO_SETTINGS_MODULE"] = "nextcloudUI.settings"

from django.core.management import execute_from_command_line

if __name__ == "__main__":
    execute_from_command_line(sys.argv)
