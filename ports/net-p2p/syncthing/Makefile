# $FreeBSD$

PORTNAME=	syncthing
PORTVERSION=	0.8.7
CATEGORIES=	net-p2p
MASTER_SITES=	https://github.com/calmh/${PORTNAME}/releases/download/v${PORTVERSION}/
DISTNAME=	${PORTNAME}-freebsd-${ARCH}-v${PORTVERSION}

MAINTAINER=	joshruehlig@gmail.com
COMMENT=	Open Source Continuous Replication / Cluster Synchronization Thing

LICENSE=	MIT

NO_BUILD=	yes
ONLY_FOR_ARCHES=	amd64
ONLY_FOR_ARCHES_REASON=	Binary builds are only provided for amd64.

PLIST_SUB=	PORTNAME=${PORTNAME} USER=${USERS} GROUP=${GROUPS}
SUB_LIST=	PORTNAME=${PORTNAME} USER=${USERS} GROUP=${GROUPS}
SUB_FILES=	pkg-message
USE_RC_SUBR=	${PORTNAME}

USERS=		sync
GROUPS=		${USERS}

.include <bsd.port.pre.mk>

do-install:
	${INSTALL_PROGRAM} ${WRKSRC}/syncthing ${STAGEDIR}${PREFIX}/bin
	${INSTALL} ${WRKSRC}/syncthing.xml.sample ${STAGEDIR}${PREFIX}/etc

.include <bsd.port.post.mk>
