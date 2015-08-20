# $FreeBSD$

PORTNAME=	mineos
PORTVERSION=	9.3.3
CATEGORIES=	games
MASTER_SITES=	#none
DISTFILES=	#none
GH_ACCOUNT=	hexparrot
GH_PROJECT=	mineos-node

MAINTAINER=	joshruehlig@gmail.com
COMMENT=	easy minecraft hosting solution

LICENSE=	GPLv3

RUN_DEPENDS=	npm:${PORTSDIR}/www/npm \
		rdiff-backup:${PORTSDIR}/sysutils/rdiff-backup \
		rsync:${PORTSDIR}/net/rsync \
		screen:${PORTSDIR}/sysutils/screen \
		git:${PORTSDIR}/devel/git

USES=		gmake
USE_JAVA=	yes
JAVA_RUN=	yes

NO_BUILD=	yes
NO_WRKSUBDIR=	yes
PLIST_SUB=	PORTNAME=${PORTNAME}
SUB_LIST=	PORTNAME=${PORTNAME} PYTHON_CMD=${PYTHON_CMD}
SUB_FILES=	pkg-message
USE_RC_SUBR=	${PORTNAME}

USERS=		mcserver
GROUPS=		${USERS}

.include <bsd.port.pre.mk>

do-install:
	${PREFIX}/bin/git clone git://github.com/${GH_ACCOUNT}/${GH_PROJECT}.git ${DATADIR}/${GH_PROJECT}
	${PREFIX}/bin/npm --prefix ${DATADIR}/${GH_PROJECT} install
#	${CP} ${DATADIR}/${GH_PROJECT}/${PORTNAME}.conf ${STAGEDIR}${PREFIX}/etc/${PORTNAME}.conf.sample

.include <bsd.port.post.mk>
