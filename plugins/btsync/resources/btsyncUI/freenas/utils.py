import hashlib
import os
import platform

btsync_pbi_path = "/usr/pbi/btsync-" + platform.machine()
btsync_etc_path = os.path.join(btsync_pbi_path, "etc")
btsync_datadirectory = "/var/db/btsync"
btsync_pidfile = "/var/run/btsync/btsync.pid"
btsync_fcgi_pidfile = "/var/run/btsync_fcgi_server.pid"
btsync_control = "/usr/local/etc/rc.d/btsync"
btsync_icon = os.path.join(btsync_pbi_path, "default.png")
btsync_oauth_file = os.path.join(btsync_pbi_path, ".oauth")


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


def get_btsync_oauth_creds():
    f = open(btsync_oauth_file)
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

btsync_settings = {
    "force_https": {
        "field": "force_https",
        "type": "checkbox",
        },
    "ssl_certificate": {
        "field": "ssl_certificate",
        "type": "textbox",
        },
    "ssl_private_key": {
        "field": "ssl_private_key",
        "type": "textbox",
         },
    "webui_port": {
        "field": "webui_port",
        "type": "textbox",
        },
}
