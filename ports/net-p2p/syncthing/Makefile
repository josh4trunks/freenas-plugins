# $FreeBSD$

PORTNAME=	syncthing
PORTVERSION=	0.9.2
CATEGORIES=	net-p2p
MASTER_SITES=	https://github.com/calmh/${PORTNAME}/releases/download/v${PORTVERSION}/
DISTNAME=	${PORTNAME}-freebsd-${CONFIG_ARCH}-v${PORTVERSION}

MAINTAINER=	joshruehlig@gmail.com
COMMENT=	Open Source Continuous Replication / Cluster Synchronization Thing

LICENSE=	MIT

NO_BUILD=	yes
ONLY_FOR_ARCHES=	amd64 i386
ONLY_FOR_ARCHES_REASON=	Binary builds are only provided for i386 and amd64.

PLIST_SUB=	PORTNAME=${PORTNAME} USER=${USERS} GROUP=${GROUPS}
SUB_LIST=	PORTNAME=${PORTNAME} USER=${USERS} GROUP=${GROUPS}
SUB_FILES=	pkg-message
USE_RC_SUBR=	${PORTNAME}

USERS=		${PORTNAME}
GROUPS=		${USERS}

.include <bsd.port.pre.mk>

.if ${ARCH} == "i386"
CONFIG_ARCH= 386
.else
CONFIG_ARCH= ${ARCH}
.endif

do-install:
	${INSTALL_PROGRAM} ${WRKSRC}/syncthing ${STAGEDIR}${PREFIX}/bin
	${INSTALL} ${WRKSRC}/syncthing.xml.sample ${STAGEDIR}${PREFIX}/etc

.include <bsd.port.post.mk>
