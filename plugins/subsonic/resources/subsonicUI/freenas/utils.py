import hashlib
import os
import platform

subsonic_pbi_path = "/usr/pbi/subsonic-" + platform.machine()
subsonic_fcgi_pidfile = "/var/run/subsonic_fcgi_server.pid"
subsonic_control = "/usr/local/etc/rc.d/subsonic"
subsonic_icon = os.path.join(subsonic_pbi_path, "default.png")
subsonic_oauth_file = os.path.join(subsonic_pbi_path, ".oauth")


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


def get_subsonic_oauth_creds():
    f = open(subsonic_oauth_file)
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

subsonic_settings = {
    "subsonic_max_memory": {
        "field": "subsonic_max_memory",
        "type": "textbox",
        },
    "subsonic_ssl": {
        "field": "subsonic_ssl",
        "type": "checkbox",
        },
    "subsonic_ssl_keystore": {
        "field": "subsonic_ssl_keystore",
        "type": "textbox",
        },
    "subsonic_ssl_password": {
        "field": "subsonic_ssl_password",
        "type": "textbox",
        },
    "subsonic_port": {
        "field": "subsonic_port",
        "type": "textbox",
        },
    "subsonic_context_path": {
        "field": "subsonic_context_path",
        "type": "textbox",
        },
}
