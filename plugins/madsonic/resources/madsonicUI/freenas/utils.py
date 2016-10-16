import hashlib
import os
import platform

madsonic_pbi_path = "/usr/pbi/madsonic-" + platform.machine()
madsonic_fcgi_pidfile = "/var/run/madsonic_fcgi_server.pid"
madsonic_control = "/usr/local/etc/rc.d/madsonic"
madsonic_icon = os.path.join(madsonic_pbi_path, "default.png")
madsonic_oauth_file = os.path.join(madsonic_pbi_path, ".oauth")


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


def get_madsonic_oauth_creds():
    f = open(madsonic_oauth_file)
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

madsonic_settings = {
    "madsonic_max_memory": {
        "field": "madsonic_max_memory",
        "type": "textbox",
        },
    "madsonic_ssl": {
        "field": "madsonic_ssl",
        "type": "checkbox",
        },
    "madsonic_ssl_keystore": {
        "field": "madsonic_ssl_keystore",
        "type": "textbox",
        },
    "madsonic_ssl_password": {
        "field": "madsonic_ssl_password",
        "type": "textbox",
        },
    "madsonic_port": {
        "field": "madsonic_port",
        "type": "textbox",
        },
    "madsonic_context_path": {
        "field": "madsonic_context_path",
        "type": "textbox",
        },
}
