# $FreeBSD$

PORTNAME=	maraschino
PORTVERSION=	9.3.1
CATEGORIES=	multimedia

MAINTAINER=	joshruehlig@gmail.com
COMMENT=	A simple web interface to act as a nice overview/front page for an XBMC HTPC.

LICENSE=	MIT

RUN_DEPENDS=	${PYTHON_PKGNAMEPREFIX}sqlite3>0:${PORTSDIR}/databases/py-sqlite3

USES=	python:2.5-2.7

USE_GITHUB=	yes
GH_ACCOUNT=	mrkipling
GH_PROJECT=	maraschino
GH_COMMIT=	ebd9222
GH_TAGNAME=	${GH_COMMIT}

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
