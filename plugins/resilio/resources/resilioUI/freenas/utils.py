import hashlib
import os
import platform

resilio_pbi_path = "/usr/pbi/resilio-" + platform.machine()
resilio_etc_path = os.path.join(resilio_pbi_path, "etc")
resilio_datadirectory = "/var/db/resilio"
resilio_fcgi_pidfile = "/var/run/resilio_fcgi_server.pid"
resilio_control = "/usr/local/etc/rc.d/resilio"
resilio_icon = os.path.join(resilio_pbi_path, "default.png")
resilio_oauth_file = os.path.join(resilio_pbi_path, ".oauth")


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


def get_resilio_oauth_creds():
    f = open(resilio_oauth_file)
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

resilio_settings = {
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
