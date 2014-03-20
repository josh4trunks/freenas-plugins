# $FreeBSD$

PORTNAME=	mineos
PORTVERSION=	2.0
CATEGORIES=	games
MASTER_SITES=	GH
USE_GITHUB=	yes
GH_ACCOUNT=	hexparrot
GH_PROJECT=	mineos
GH_COMMIT=	75f2d6d
GH_TAGNAME=	${GH_COMMIT}

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
WRKSRC=		${WRKDIR}/${GH_ACCOUNT}-${GH_PROJECT}-${GH_COMMIT}
PLIST_SUB=	PORTNAME=${PORTNAME}
SUB_LIST=	PORTNAME=${PORTNAME} PYTHON_CMD=${PYTHON_CMD}
SUB_FILES=	pkg-message
USE_RC_SUBR=	${PORTNAME}

.include <bsd.port.pre.mk>

do-install:
	${MKDIR} -p ${STAGEDIR}${DATADIR}/mineos
	cd ${WRKSRC} && ${COPYTREE_SHARE} \* ${STAGEDIR}${DATADIR}/mineos
	${CP} ${STAGEDIR}${DATADIR}/mineos/${PORTNAME}.conf ${STAGEDIR}${PREFIX}/etc/${PORTNAME}.conf.sample
	${REINPLACE_CMD} -e 's!\(misc.require_https = \)True!\1 False!' ${STAGEDIR}${PREFIX}/etc/${PORTNAME}.conf.sample

.include <bsd.port.post.mk>
