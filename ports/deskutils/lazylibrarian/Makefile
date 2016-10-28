# $FreeBSD$

PORTNAME=	lazylibrarian
PORTVERSION=	9.3.0
CATEGORIES=	deskutils

MAINTAINER=	joshruehlig@gmail.com
COMMENT=	An automated book downloader for SABnzbd.

LICENSE=	GPLv3

RUN_DEPENDS=	${PYTHON_PKGNAMEPREFIX}sqlite3>0:${PORTSDIR}/databases/py-sqlite3

USES=	python:2.6-2.7

USE_GITHUB=     yes
GH_ACCOUNT=     DobyTang
GH_PROJECT=     LazyLibrarian
GH_COMMIT=      6c5945e
GH_TAGNAME=     ${GH_COMMIT}

NO_BUILD=	yes
PLIST_SUB=	PORTNAME=${PORTNAME} USERS=${USERS} GROUPS=${GROUPS}
SUB_LIST=	PORTNAME=${PORTNAME} USERS=${USERS} GROUPS=${GROUPS} PYTHON_CMD=${PYTHON_CMD}
SUB_FILES=	pkg-message
USE_RC_SUBR=	${PORTNAME}

USERS=		media
GROUPS=		${USERS}

.include <bsd.port.pre.mk>

do-install:
	${MKDIR} ${STAGEDIR}${DATADIR}/${GH_PROJECT}
	cd ${WRKSRC} && ${COPYTREE_SHARE} . ${STAGEDIR}${DATADIR}/${GH_PROJECT}

.include <bsd.port.post.mk>
