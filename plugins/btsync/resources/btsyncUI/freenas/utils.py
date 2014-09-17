from subprocess import Popen, PIPE
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
    return 'http%s://%s:%s/plugins/json-rpc/v1/' % (
        's' if request.is_secure() else '',
        request.META.get("SERVER_ADDR"),
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
    "webui_port": {
        "field": "webui_port",
        "type": "textbox",
        },
    "config_refresh_interval": {
        "field": "config_refresh_interval",
        "type": "textbox",
        },
    "disk_low_priority": {
        "field": "disk_low_priority",
        "type": "checkbox",
        },
    "external_port": {
        "field": "external_port",
        "type": "textbox",
        },
    "folder_rescan_interval": {
        "field": "folder_rescan_interval",
        "type": "textbox",
        },
    "lan_encrypt_data": {
        "field": "lan_encrypt_data",
        "type": "checkbox",
        },
    "log_size": {
        "field": "log_size",
        "type": "textbox",
        },
    "max_file_size_diff_for_patching": {
        "field": "max_file_size_diff_for_patching",
        "type": "textbox",
        },
    "max_file_size_for_versioning": {
        "field": "max_file_size_for_versioning",
        "type": "textbox",
        },
    "peer_expiration_days": {
        "field": "peer_expiration_days",
        "type": "textbox",
        },
    "rate_limit_local_peers": {
        "field": "rate_limit_local_peers",
        "type": "checkbox",
        },
    "sync_max_time_diff": {
        "field": "sync_max_time_diff",
        "type": "textbox",
        },
    "sync_trash_ttl": {
        "field": "sync_trash_ttl",
        "type": "textbox",
        },
}
