# $FreeBSD$

PORTNAME=	mylar
PORTVERSION=	9.3.2
CATEGORIES=	deskutils

MAINTAINER=	joshruehlig@gmail.com
COMMENT=	An automated Comic Book downloader (cbr/cbz) trying to follow in the lines of sickbeard and headphones.

LICENSE=	GPLv3

RUN_DEPENDS=	${PYTHON_PKGNAMEPREFIX}sqlite3>0:${PORTSDIR}/databases/py-sqlite3

USES=	python:2.7

USE_GITHUB=     yes
GH_ACCOUNT=     evilhero
GH_PROJECT=     mylar
GH_COMMIT=      83dc652
GH_TAGNAME=     ${GH_COMMIT}

NO_BUILD=	yes
PLIST_SUB=	PORTNAME=${PORTNAME} USERS=${USERS} GROUPS=${GROUPS}
SUB_LIST=	PORTNAME=${PORTNAME} USERS=${USERS} GROUPS=${GROUPS} PYTHON_CMD=${PYTHON_CMD}
SUB_FILES=	pkg-message
USE_RC_SUBR=	${PORTNAME}

USERS=		media
GROUPS=		${USERS}

OPTIONS_DEFINE=	OPENSSL
OPTIONS_DEFAULT=	OPENSSL

OPENSSL_RUN_DEPENDS=	${PYTHON_PKGNAMEPREFIX}openssl>0:${PORTSDIR}/security/py-openssl

.include <bsd.port.pre.mk>

do-install:
	${MKDIR} ${STAGEDIR}${DATADIR}/${GH_PROJECT}
	cd ${WRKSRC} && ${COPYTREE_SHARE} . ${STAGEDIR}${DATADIR}/${GH_PROJECT}

.include <bsd.port.post.mk>
