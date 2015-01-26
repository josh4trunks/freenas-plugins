# $FreeBSD$

PORTNAME=	sonarr
PORTVERSION=	2.0.0.2663
CATEGORIES=	multimedia
MASTER_SITES=	http://download.sonarr.tv/v2/master/mono/
DISTNAME=	NzbDrone.master.${PORTVERSION}.mono

MAINTAINER=	joshruehlig@gmail.com
COMMENT=	Smart PVR for newsgroup and bittorrent users.

LICENSE=	GPLv3

LIB_DEPENDS=	libsqlite3.so:${PORTSDIR}/databases/sqlite3 \
		libmediainfo.so:${PORTSDIR}/multimedia/libmediainfo

USES=		mono

WRKSRC=		${WRKDIR}/NzbDrone
NO_BUILD=	yes
PLIST_SUB=	PORTNAME=${PORTNAME} USER=${USERS} GROUP=${GROUPS}
SUB_LIST=	PORTNAME=${PORTNAME} USER=${USERS} GROUP=${GROUPS}
SUB_FILES=	pkg-message
USE_RC_SUBR=	${PORTNAME}

USERS=		media
GROUPS=		${USERS}

do-install:
	${INSTALL} -d ${STAGEDIR}${DATADIR}/NzbDrone
	cd ${WRKSRC} && ${COPYTREE_SHARE} . ${STAGEDIR}${DATADIR}/NzbDrone

.include <bsd.port.mk>
