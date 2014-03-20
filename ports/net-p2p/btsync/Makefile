# $FreeBSD$

PORTNAME=	btsync
PORTVERSION=	1.2.91
CATEGORIES=	net-p2p
MASTER_SITES=   http://syncapp.bittorrent.com/${PORTVERSION}/
DISTNAME=       ${PORTNAME}_freebsd_${CONFIG_ARCH}-${PORTVERSION}

MAINTAINER=     joshruehlig@gmail.com
COMMENT=        Distributed peer-to-peer file syncing application.

.include <bsd.port.options.mk>
.if ${ARCH} == "amd64"
CONFIG_ARCH=	x64
.else
CONFIG_ARCH=	${ARCH}
.endif

LICENSE=	EULA
LICENSE_NAME=	BitTorrent Sync
LICENSE_FILE=	${WRKSRC}/LICENSE.TXT
LICENSE_PERMS=	# Any copying or redistribution of the Software is prohibited.


NO_WRKSUBDIR=	yes
NO_BUILD=	yes
ONLY_FOR_ARCHES=	amd64 i386
ONLY_FOR_ARCHES_REASON=	It is a binary-only program. Source code not available.

PLIST_SUB=	PORTNAME=${PORTNAME} USER=${USERS} GROUP=${GROUPS}
SUB_LIST=	PORTNAME=${PORTNAME} USER=${USERS} GROUP=${GROUPS}
SUB_FILES=	pkg-message
USE_RC_SUBR=	${PORTNAME}

USERS=		${PORTNAME}
GROUPS=		${USERS}

.include <bsd.port.pre.mk>

post-extract:
	${MKDIR} ${WRKSRC}/temp
	${MV} ${WRKSRC}/${PORTNAME} ${WRKSRC}/temp

do-install:
	${INSTALL_PROGRAM} ${WRKSRC}/temp/btsync ${STAGEDIR}${PREFIX}/bin
	${INSTALL} -d ${STAGEDIR}/${ETCDIR}
	${WRKSRC}/temp/btsync --dump-sample-config > ${STAGEDIR}/${ETCDIR}/config.ini.sample
	${REINPLACE_CMD} -e 's;\(^ *"storage_path" \)/.*",;\1${ETCDIR}",;' ${STAGEDIR}/${ETCDIR}/config.ini.sample

.include <bsd.port.post.mk>
