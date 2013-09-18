import os
import platform

owncloud_pbi_path = "/usr/pbi/owncloud-" + platform.machine()
owncloud_etc_path = os.path.join(owncloud_pbi_path, "etc")
owncloud_mnt_path = os.path.join(owncloud_pbi_path, "mnt")
owncloud_fcgi_pidfile = "/var/run/owncloud_fcgi_server.pid"
owncloud_fcgi_wwwdir = os.path.join(owncloud_pbi_path, "www")
owncloud_control = "/usr/local/etc/rc.d/apache22"
owncloud_icon = os.path.join(owncloud_pbi_path, "default.png")
owncloud_oauth_file = os.path.join(owncloud_pbi_path, ".oauth")


def get_rpc_url(request):
    return 'http%s://%s:%s/plugins/json-rpc/v1/' % (
        's' if request.is_secure() else '',
        request.META.get("SERVER_ADDR"),
        request.META.get("SERVER_PORT"),
        )


def get_owncloud_oauth_creds():
    f = open(owncloud_oauth_file)
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
