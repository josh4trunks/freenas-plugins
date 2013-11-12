from subprocess import Popen, PIPE
import hashlib
import os
import platform

gamez_pbi_path = "/usr/pbi/gamez-" + platform.machine()
gamez_etc_path = os.path.join(gamez_pbi_path, "etc")
gamez_fcgi_pidfile = "/var/run/gamez_fcgi_server.pid"
gamez_control = "/usr/local/etc/rc.d/gamez"
gamez_icon = os.path.join(gamez_pbi_path, "default.png")
gamez_oauth_file = os.path.join(gamez_pbi_path, ".oauth")


def get_rpc_url(request):
    return 'http%s://%s:%s/plugins/json-rpc/v1/' % (
        's' if request.is_secure() else '',
        request.META.get("SERVER_ADDR"),
        request.META.get("SERVER_PORT"),
        )


def get_gamez_oauth_creds():
    f = open(gamez_oauth_file)
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
