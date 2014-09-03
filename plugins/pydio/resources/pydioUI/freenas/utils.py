import os
import platform

pydio_pbi_path = "/usr/pbi/pydio-" + platform.machine()
pydio_etc_path = os.path.join(pydio_pbi_path, "etc")
pydio_mnt_path = os.path.join(pydio_pbi_path, "mnt")
pydio_fcgi_pidfile = "/var/run/pydio_fcgi_server.pid"
pydio_fcgi_wwwdir = os.path.join(pydio_pbi_path, "www")
pydio_control = "/usr/local/etc/rc.d/apache24"
pydio_icon = os.path.join(pydio_pbi_path, "default.png")
pydio_oauth_file = os.path.join(pydio_pbi_path, ".oauth")


def get_rpc_url(request):
    addr = request.META.get("SERVER_ADDR")
    # IPv6
    if ':' in addr:
        addr = '[%s]' % addr
    return 'http%s://%s:%s/plugins/json-rpc/v1/' % (
        's' if request.is_secure() else '',
        addr,
        request.META.get("SERVER_PORT"),
    )


def get_pydio_oauth_creds():
    f = open(pydio_oauth_file)
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
