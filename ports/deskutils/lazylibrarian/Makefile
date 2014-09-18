# $FreeBSD$

PORTNAME=	lazylibrarian
PORTVERSION=	2.1
CATEGORIES=	deskutils
MASTER_SITES=	GH

MAINTAINER=	joshruehlig@gmail.com
COMMENT=	An automated book downloader for SABnzbd.

LICENSE=	GPLv3 PSFL
LICENSE_COMB=	multi

RUN_DEPENDS=	${PYTHON_PKGNAMEPREFIX}sqlite3>0:${PORTSDIR}/databases/py-sqlite3

USES=	python:2.6-2.7

USE_GITHUB=     yes
GH_ACCOUNT=     DobyTang
GH_PROJECT=     LazyLibrarian
GH_COMMIT=      aff78ec
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
	${MKDIR} ${STAGEDIR}${DATADIR}/LazyLibrarian
	cd ${WRKSRC} && ${COPYTREE_SHARE} \* ${STAGEDIR}${DATADIR}/LazyLibrarian

.include <bsd.port.post.mk>
