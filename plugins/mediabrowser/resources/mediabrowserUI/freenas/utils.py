import hashlib
import os
import platform

mediabrowser_pbi_path = "/usr/pbi/mediabrowser-" + platform.machine()
mediabrowser_fcgi_pidfile = "/var/run/mediabrowser_fcgi_server.pid"
mediabrowser_control = "/usr/local/etc/rc.d/mediabrowser"
mediabrowser_icon = os.path.join(mediabrowser_pbi_path, "default.png")
mediabrowser_oauth_file = os.path.join(mediabrowser_pbi_path, ".oauth")


def get_rpc_url(request):
    return 'http%s://%s:%s/plugins/json-rpc/v1/' % (
        's' if request.is_secure() else '',
        request.META.get("SERVER_ADDR"),
        request.META.get("SERVER_PORT"),
        )


def get_mediabrowser_oauth_creds():
    f = open(mediabrowser_oauth_file)
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
