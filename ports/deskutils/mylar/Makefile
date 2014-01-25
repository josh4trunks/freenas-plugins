# $FreeBSD$

PORTNAME=	mylar
PORTVERSION=	2.0
CATEGORIES=	deskutils
MASTER_SITES=	GH

MAINTAINER=	joshruehlig@gmail.com
COMMENT=	An automated Comic Book downloader (cbr/cbz) trying to follow in the lines of sickbeard and headphones.

LICENSE=	GPLv3 PSFL
LICENSE_COMB=	multi

RUN_DEPENDS=	${PYTHON_PKGNAMEPREFIX}sqlite3>0:${PORTSDIR}/databases/py-sqlite3

USE_PYTHON=	2.7

USE_GITHUB=     yes
GH_ACCOUNT=     evilhero
GH_PROJECT=     mylar
GH_COMMIT=      250630a
GH_TAGNAME=     ${GH_COMMIT}

NO_BUILD=	yes
WRKSRC=		${WRKDIR}/${GH_ACCOUNT}-${GH_PROJECT}-${GH_COMMIT}
PLIST_SUB=	PORTNAME=${PORTNAME} USER=${USERS} GROUP=${GROUPS}
SUB_LIST=	PORTNAME=${PORTNAME} USER=${USERS} GROUP=${GROUPS} PYTHON_CMD=${PYTHON_CMD}
SUB_FILES=	pkg-message
USE_RC_SUBR=	${PORTNAME}

USERS=		media
GROUPS=		media

.include <bsd.port.pre.mk>

do-install:
	${INSTALL} -d ${STAGEDIR}${DATADIR}
	${MKDIR} ${STAGEDIR}${DATADIR}/mylar
	cd ${WRKSRC} && ${COPYTREE_SHARE} \* ${STAGEDIR}${DATADIR}/mylar

.include <bsd.port.post.mk>
