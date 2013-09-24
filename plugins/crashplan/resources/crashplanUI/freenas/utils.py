import os
import platform

crashplan_pbi_path = "/usr/pbi/crashplan-" + platform.machine()
crashplan_etc_path = os.path.join(crashplan_pbi_path, "etc")
crashplan_mnt_path = os.path.join(crashplan_pbi_path, "mnt")
crashplan_fcgi_pidfile = "/var/run/crashplan_fcgi_server.pid"
crashplan_fcgi_wwwdir = os.path.join(crashplan_pbi_path, "www")
crashplan_control = "/usr/local/etc/rc.d/crashplan"
crashplan_icon = os.path.join(crashplan_pbi_path, "default.png")
crashplan_oauth_file = os.path.join(crashplan_pbi_path, ".oauth")


def get_rpc_url(request):
    return 'http%s://%s:%s/plugins/json-rpc/v1/' % (
        's' if request.is_secure() else '',
        request.META.get("SERVER_ADDR"),
        request.META.get("SERVER_PORT"),
        )


def get_crashplan_oauth_creds():
    f = open(crashplan_oauth_file)
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
