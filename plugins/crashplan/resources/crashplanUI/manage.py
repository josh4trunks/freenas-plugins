#!/usr/bin/env python

import os
import sys
import platform

arch = platform.machine()
python_major = sys.version_info.major
python_minor = sys.version_info.minor
python = "python%d.%d" % (python_major, python_minor)

PBI_PATH = "/usr/pbi/crashplan-%s" % arch
PBI_UI = os.path.join(PBI_PATH, "crashplanUI")
PYTHON_SITE_PACKAGES = os.path.join(PBI_PATH,
    "lib/%s/site-packages" % python)

sys.path.append(PYTHON_SITE_PACKAGES)
sys.path.append(PBI_PATH)
sys.path.append(PBI_UI)

os.environ["DJANGO_SETTINGS_MODULE"] = "crashplanUI.settings"

from django.core.management import execute_from_command_line

if __name__ == "__main__":
    execute_from_command_line(sys.argv)
