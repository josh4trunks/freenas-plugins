#!/bin/sh

lazylibrarian_pbi_path=/usr/pbi/lazylibrarian-$(uname -m)

${lazylibrarian_pbi_path}/bin/python ${lazylibrarian_pbi_path}/lazylibrarianUI/manage.py syncdb --migrate --noinput
