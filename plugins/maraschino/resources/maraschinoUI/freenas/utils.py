from subprocess import Popen, PIPE
import hashlib
import os
import platform

maraschino_pbi_path = "/usr/pbi/maraschino-" + platform.machine()
maraschino_etc_path = os.path.join(maraschino_pbi_path, "etc")
maraschino_fcgi_pidfile = "/var/run/maraschino_fcgi_server.pid"
maraschino_control = "/usr/local/etc/rc.d/maraschino"
maraschino_icon = os.path.join(maraschino_pbi_path, "default.png")
maraschino_oauth_file = os.path.join(maraschino_pbi_path, ".oauth")


def get_rpc_url(request):
    return 'http%s://%s:%s/plugins/json-rpc/v1/' % (
        's' if request.is_secure() else '',
        request.META.get("SERVER_ADDR"),
        request.META.get("SERVER_PORT"),
        )


def get_maraschino_oauth_creds():
    f = open(maraschino_oauth_file)
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
