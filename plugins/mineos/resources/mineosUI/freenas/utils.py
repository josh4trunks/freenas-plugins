from subprocess import Popen, PIPE
import hashlib
import os
import platform

mineos_pbi_path = "/usr/pbi/mineos-" + platform.machine()
mineos_etc_path = os.path.join(mineos_pbi_path, "etc")
mineos_fcgi_pidfile = "/var/run/mineos_fcgi_server.pid"
mineos_control = "/usr/local/etc/rc.d/mineos"
mineos_icon = os.path.join(mineos_pbi_path, "default.png")
mineos_oauth_file = os.path.join(mineos_pbi_path, ".oauth")


def get_rpc_url(request):
    return 'http%s://%s:%s/plugins/json-rpc/v1/' % (
        's' if request.is_secure() else '',
        request.META.get("SERVER_ADDR"),
        request.META.get("SERVER_PORT"),
        )


def get_mineos_oauth_creds():
    f = open(mineos_oauth_file)
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

mineos_settings = {
    "mineos_ssl": {
        "field": "mineos_ssl",
        "type": "checkbox",
    },
    "mineos_cert": {
        "field": "mineos_cert",
        "type": "textbox",
    },
    "mineos_key": {
        "field": "mineos_key",
        "type": "textbox",
    },
    "mineos_port": {
        "field": "mineos_port",
        "type": "textbox",
    },
    "mineos_mask": {
        "field": "mineos_mask",
        "type": "checkbox",
    },
    "mineos_locale": {
        "field": "mineos_locale",
        "type": "textbox",
    },
    "mineos_delay": {
        "field": "mineos_delay",
        "type": "textbox",
    },
    "mineos_basedir": {
        "field": "mineos_basedir",
        "type": "textbox",
    },
    "mineos_log": {
        "field": "mineos_log",
        "type": "textbox",
    },
}
