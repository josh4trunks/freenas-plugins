import hashlib
import os
import platform

xmrig_pbi_path = "/usr/pbi/xmrig-" + platform.machine()
xmrig_etc_path = os.path.join(xmrig_pbi_path, "etc")
xmrig_etc_dir = os.path.join(xmrig_etc_path, "xmrig")
xmrig_fcgi_pidfile = "/var/run/xmrig_fcgi_server.pid"
xmrig_control = "/usr/local/etc/rc.d/xmrig"
xmrig_icon = os.path.join(xmrig_pbi_path, "default.png")
xmrig_oauth_file = os.path.join(xmrig_pbi_path, ".oauth")


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


def get_xmrig_oauth_creds():
    f = open(xmrig_oauth_file)
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

xmrig_settings = {
    "algo": {
        "field": "algo",
        "type": "textbox",
        },
    "variant": {  
        "field": "variant",
        "type": "textbox",
        },
    "url": {
        "field": "url",
        "type": "textbox",
        },
    "user": {
        "field": "user",
        "type": "textbox",
        },
    "password": {
        "field": "pass",
        "type": "textbox",
        },
    "rig_id": {
        "field": "rig-id",
        "type": "textbox",
        },
    "user_agent": {
        "field": "user-agent",
        "type": "textbox",
        },
    "keepalive": {
        "field": "keepalive",
        "type": "checkbox",
        },
    "nicehash": {
        "field": "nicehash",
        "type": "checkbox",
        },
    "av": {
        "field": "av",
        "type": "textbox",
        },
    "threads": {
        "field": "threads",
        "type": "textbox",
        },
    "safe": {
        "field": "safe",
        "type": "checkbox",
        },
    "cpu_affinity": {
        "field": "cpu-affinity",
        "type": "textbox",
        },
    "max_cpu_usage": {
        "field": "max-cpu-usage",
        "type": "textbox",
        },
    "cpu_priority": {
        "field": "cpu-priority",
        "type": "textbox",
        },
    "donate_level": {
        "field": "donate-level",
        "type": "textbox",
        },
    "port": {
        "field": "port",
        "type": "textbox",
        },
    "access_token": {
        "field": "access-token",
        "type": "textbox",
        },
    "worker_id": {
        "field": "worker-id",
        "type": "textbox",
        },
    "ipv6": {
        "field": "ipv6",
        "type": "checkbox",
        },
    "restricted": {
        "field": "restricted",
        "type": "checkbox",
        },
}
