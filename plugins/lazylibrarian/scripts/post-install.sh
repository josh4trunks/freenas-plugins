#!/bin/sh

lazylibrarian_pbi_path=/usr/pbi/lazylibrarian-$(uname -m)

${lazylibrarian_pbi_path}/bin/python2.7 ${lazylibrarian_pbi_path}/lazylibrarianUI/manage.py syncdb --migrate --noinput

install -o media -g media -d /var/db/lazylibrarian
