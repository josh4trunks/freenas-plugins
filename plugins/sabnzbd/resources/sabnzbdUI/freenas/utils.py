from subprocess import Popen, PIPE
import hashlib
import os
import platform

sabnzbd_pbi_path = "/usr/pbi/sabnzbd-" + platform.machine()
sabnzbd_etc_path = os.path.join(sabnzbd_pbi_path, "etc")
sabnzbd_mnt_path = os.path.join(sabnzbd_pbi_path, "mnt")
sabnzbd_fcgi_pidfile = "/var/run/sabnzbd_fcgi_server.pid"
sabnzbd_fcgi_wwwdir = os.path.join(sabnzbd_pbi_path, "www")
sabnzbd_control = "/usr/local/etc/rc.d/sabnzbd"
sabnzbd_icon = os.path.join(sabnzbd_pbi_path, "default.png")
sabnzbd_oauth_file = os.path.join(sabnzbd_pbi_path, ".oauth")


def get_rpc_url(request):
    return 'http%s://%s:%s/plugins/json-rpc/v1/' % (
        's' if request.is_secure() else '',
        request.META.get("SERVER_ADDR"),
        request.META.get("SERVER_PORT"),
        )


def get_sabnzbd_oauth_creds():
    f = open(sabnzbd_oauth_file)
    lines = f.readlines()
    f.close()

    key = secret = None
    for l in lines:
        l = l.strip()

        if l.startswith("key"):
            pair = l.split("=")
            if len(pair) > 1:
                key = pair[1].strip()

        elif l.startswith("secret"):
            pair = l.split("=")
            if len(pair) > 1:
                secret = pair[1].strip()

    return key, secret
