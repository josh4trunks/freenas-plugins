import os
import sys
import signal

import daemon
from flup.server.fcgi import WSGIServer

HERE = os.path.abspath(os.path.dirname(__file__))
sys.path.insert(0, os.path.join(HERE, "lib/python2.7/site-packages"))
owncloud_fcgi_pidfile = "/var/run/owncloud_fcgi_server.pid"


def owncloud_fcgi_start(args):
    if len(args) < 2:
        return False

    ip = args[0]
    port = long(args[1])

    os.environ['DJANGO_SETTINGS_MODULE'] = 'owncloudUI.settings'
    import django.core.handlers.wsgi
    app = django.core.handlers.wsgi.WSGIHandler()

    res = False
    with open(owncloud_fcgi_pidfile, "wb") as fp:
        fp.write(str(os.getpid()))
        fp.close()

        res = WSGIServer(app, bindAddress=(ip, port)).run()

    return res


def owncloud_fcgi_stop(args):
    res = False
    if os.access(owncloud_fcgi_pidfile, os.F_OK):
        with open(owncloud_fcgi_pidfile, "r") as fp:
            pid = long(fp.read())
            fp.close()

            os.kill(pid, signal.SIGHUP)
            res = True

    if os.access(owncloud_fcgi_pidfile, os.F_OK):
        os.unlink(owncloud_fcgi_pidfile)

    return res


def owncloud_fcgi_status(args):
    res = False
    if os.access(owncloud_fcgi_pidfile, os.F_OK):
        with open(owncloud_fcgi_pidfile, "r") as fp:
            pid = long(fp.read())
            fp.close()
            res = True

    return res


def owncloud_fcgi_configure(args):
    return True


def main(argc, argv):
    if argc < 2:
        sys.exit(1)

    commands = {
        'start': owncloud_fcgi_start,
        'stop': owncloud_fcgi_stop,
        'status': owncloud_fcgi_status,
        'configure': owncloud_fcgi_configure
    }

    with daemon.DaemonContext():
        if not commands.has_key(argv[0]):
            sys.exit(1)

        if not commands[argv[0]](argv[1:]):
            sys.exit(1)

    sys.exit(0)

if __name__ == '__main__':
    main(len(sys.argv), sys.argv[1:])
