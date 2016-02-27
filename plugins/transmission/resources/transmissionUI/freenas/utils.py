import hashlib
import os
import platform

transmission_pbi_path = "/usr/pbi/transmission-" + platform.machine()
transmission_conf_dir = "/var/db/transmission"
transmission_fcgi_pidfile = "/var/run/transmission_fcgi_server.pid"
transmission_control = "/usr/local/etc/rc.d/transmission"
transmission_icon = os.path.join(transmission_pbi_path, "default.png")
transmission_oauth_file = os.path.join(transmission_pbi_path, ".oauth")


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


def get_transmission_oauth_creds():
    f = open(transmission_oauth_file)
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

transmission_settings = {
    "incomplete_dir": {
        "field": "incomplete-dir",
        "type": "textbox",
        },
    "watch_dir": {
        "field": "watch-dir",
        "type": "textbox",
        },
    "script_torrent_done": {
        "field": "script-torrent-done-filename",
        "type": "textbox",
         },
    "rpc_port": {
        "field": "rpc-port",
        "type": "textbox",
        },
    "rpc_auth": {
        "field": "rpc-enabled",
        "type": "checkbox",
        },
    "rpc_auth_required": {
        "field": "rpc-authentication-required",
        "type": "checkbox",
        },
    "rpc_username": {
        "field": "rpc-username",
        "type": "textbox",
        },
    "rpc_password": {
        "field": "rpc-password",
        "type": "textbox",
        "filter": lambda x: '{' + hashlib.sha1(x).hexdigest()
        },
    "rpc_whitelist": {
        "field": "rpc-whitelist",
        "type": "textbox",
        },
    "utp": {
        "field": "utp-enabled",
        "type": "checkbox",
        },
    "cache_size": {
        "field": "cache-size-mb",
        "type": "textbox",
        },
    "permissions": {
        "field": "umask",
        "type": "textbox",
        }
}
