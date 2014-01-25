# $FreeBSD$

PORTNAME=	btsync
PORTVERSION=	1.2.82
CATEGORIES=	net-p2p
MASTER_SITES=   http://syncapp.bittorrent.com/${PORTVERSION}/
DISTNAME=       ${PORTNAME}_freebsd_${CONFIG_ARCH}-${PORTVERSION}

MAINTAINER=     joshruehlig@gmail.com
COMMENT=        Distributed peer-to-peer file syncing application.

.include <bsd.port.options.mk>
.if ${ARCH} == "amd64"
CONFIG_ARCH=	x64
.endif

LICENSE=	EULA
LICENSE_NAME=  BitTorrent Sync
LICENSE_FILE=  ${WRKSRC}/LICENSE.TXT
LICENSE_PERMS= auto-accept

NO_WRKSUBDIR=	yes
NO_BUILD=	yes
ONLY_FOR_ARCHES=	amd64 i386
ONLY_FOR_ARCHES_REASON=	It is a binary-only program. Source code not available.

PLIST_SUB=	PORTNAME=${PORTNAME} USER=${USERS} GROUP=${GROUPS}
SUB_LIST=	PORTNAME=${PORTNAME} USER=${USERS} GROUP=${GROUPS}
SUB_FILES=	pkg-message
USE_RC_SUBR=	${PORTNAME}

USERS=		${PORTNAME}
GROUPS=		${PORTNAME}

.include <bsd.port.pre.mk>

post-extract:
	${MKDIR} ${WRKSRC}/temp
	${MV} ${WRKSRC}/${PORTNAME} ${WRKSRC}/temp

post-patch:
	@${REINPLACE_CMD} -e 's!%%ETCDIR%%!${ETCDIR}!' ${WRKSRC}/config.ini.sample

do-install:
	${INSTALL_PROGRAM} ${WRKSRC}/temp/${PORTNAME} ${STAGEDIR}${PREFIX}/bin
	${INSTALL} -d ${STAGEDIR}/${ETCDIR}
	${INSTALL} ${WRKSRC}/config.ini.sample ${STAGEDIR}/${ETCDIR}

.include <bsd.port.post.mk>
