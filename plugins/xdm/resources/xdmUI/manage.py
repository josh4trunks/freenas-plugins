#!/usr/bin/env python

import os
import sys
import platform

arch = platform.machine()
python_major = sys.version_info.major
python_minor = sys.version_info.minor
python = "python%d.%d" % (python_major, python_minor)

XDM_PATH = "/usr/pbi/xdm-%s" % arch
XDM_UI = os.path.join(XDM_PATH, "xdmUI")
PYTHON_SITE_PACKAGES = os.path.join(XDM_PATH,"lib/%s/site-packages" % python)

sys.path.append(PYTHON_SITE_PACKAGES)
sys.path.append(XDM_PATH)
sys.path.append(XDM_UI)

os.environ["DJANGO_SETTINGS_MODULE"] = "xdmUI.settings"

from django.core.management import execute_from_command_line

if __name__ == "__main__":
    execute_from_command_line(sys.argv)
