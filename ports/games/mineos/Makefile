# $FreeBSD$

PORTNAME=	mineos
PORTVERSION=	2.0
CATEGORIES=	games
MASTER_SITES=	#none
DISTFILES=	#none
GH_ACCOUNT=	hexparrot
GH_PROJECT=	mineos

MAINTAINER=	joshruehlig@gmail.com
COMMENT=	easy minecraft hosting solution

LICENSE=	GPLv3

RUN_DEPENDS=	wget:${PORTSDIR}/ftp/wget \
		rdiff-backup:${PORTSDIR}/sysutils/rdiff-backup \
		rsync:${PORTSDIR}/net/rsync \
		screen:${PORTSDIR}/sysutils/screen \
		${PYTHON_PKGNAMEPREFIX}cherrypy>0:${PORTSDIR}/www/py-cherrypy \
		git:${PORTSDIR}/devel/git

USE_PYTHON=	2.7
USE_JAVA=	yes
JAVA_VERSION=	1.7
JAVA_RUN=	yes

NO_BUILD=	yes
NO_WRKSUBDIR=	yes
PLIST_SUB=	PORTNAME=${PORTNAME}
SUB_LIST=	PORTNAME=${PORTNAME} PYTHON_CMD=${PYTHON_CMD}
SUB_FILES=	pkg-message
USE_RC_SUBR=	${PORTNAME}

.include <bsd.port.pre.mk>

do-install:

post-install:
	${PREFIX}/bin/git clone git://github.com/${GH_ACCOUNT}/${GH_PROJECT}.git ${DATADIR}/mineos
	${CP} ${DATADIR}/mineos/${PORTNAME}.conf ${PREFIX}/etc/${PORTNAME}.conf.sample
	${REINPLACE_CMD} -e 's:\(^misc.require_https *= *\)True:\1False:' ${PREFIX}/etc/${PORTNAME}.conf.sample
	${RM} ${PREFIX}/etc/${PORTNAME}.conf.sample.bak

.include <bsd.port.post.mk>
