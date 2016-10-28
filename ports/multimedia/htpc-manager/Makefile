# $FreeBSD$

PORTNAME=	htpc-manager
PORTVERSION=	autoupdate.9
PORTREVISION=	2
CATEGORIES=	multimedia

MAINTAINER=	joshruehlig@gmail.com
COMMENT=	Htpc Manager combines all your favorite software into one slick interface.

LICENSE=	MIT

RUN_DEPENDS=	${PYTHON_PKGNAMEPREFIX}sqlite3>0:${PORTSDIR}/databases/py-sqlite3 \
		${PYTHON_PKGNAMEPREFIX}psutil>0:${PORTSDIR}/sysutils/py-psutil

USES=	python:2.7

USE_GITHUB=     yes
GH_ACCOUNT=     Hellowlol
GH_PROJECT=     HTPC-Manager
GH_COMMIT=      9efb173
GH_TAGNAME=     ${GH_COMMIT}

NO_BUILD=	yes
PLIST_SUB=	PORTNAME=${PORTNAME} USERS=${USERS} GROUPS=${GROUPS}
SUB_LIST=	PORTNAME=${PORTNAME} USERS=${USERS} GROUPS=${GROUPS} PYTHON_CMD=${PYTHON_CMD}
SUB_FILES=	pkg-message
USE_RC_SUBR=	${PORTNAME}

USERS=		media
GROUPS=		${USERS}

OPTIONS_DEFINE=	OPENSSL PIL
OPTIONS_DEFAULT=	OPENSSL PIL
PIL_DESC=	convert and resize images retrieved from the XBMC API

OPENSSL_RUN_DEPENDS=	${PYTHON_PKGNAMEPREFIX}openssl>0:${PORTSDIR}/security/py-openssl
PIL_RUN_DEPENDS=	${PYTHON_PKGNAMEPREFIX}imaging>0:${PORTSDIR}/graphics/py-imaging

.include <bsd.port.pre.mk>

do-install:
	${MKDIR} ${STAGEDIR}${DATADIR}/${GH_PROJECT}
	cd ${WRKSRC} && ${COPYTREE_SHARE} . ${STAGEDIR}${DATADIR}/${GH_PROJECT}

.include <bsd.port.post.mk>
