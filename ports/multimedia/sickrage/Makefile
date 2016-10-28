# $FreeBSD$

PORTNAME=	sickrage
PORTVERSION=	autoupdate.9
PORTREVISION=	1
CATEGORIES=	multimedia

MAINTAINER=	joshruehlig@gmail.com
COMMENT=	Video File Manager for TV Shows

LICENSE=	GPLv3

RUN_DEPENDS=	${PYTHON_PKGNAMEPREFIX}utils>0:${PORTSDIR}/devel/py-utils \
		${PYTHON_PKGNAMEPREFIX}sqlite3>0:${PORTSDIR}/databases/py-sqlite3 \
		${PYTHON_PKGNAMEPREFIX}imaging>0:${PORTSDIR}/graphics/py-imaging \
		${PYTHON_PKGNAMEPREFIX}lxml>0:${PORTSDIR}/devel/py-lxml

USES=	python:2.7

USE_GITHUB=     yes
GH_ACCOUNT=     SickRage
GH_PROJECT=     SickRage
GH_COMMIT=      a89bf7f
GH_TAGNAME=     ${GH_COMMIT}

NO_BUILD=	yes
PLIST_SUB=	PORTNAME=${PORTNAME} USERS=${USERS} GROUPS=${GROUPS}
SUB_LIST=	PORTNAME=${PORTNAME} USERS=${USERS} GROUPS=${GROUPS} PYTHON_CMD=${PYTHON_CMD}
SUB_FILES=	pkg-message
USE_RC_SUBR=	${PORTNAME}

USERS=		media
GROUPS=		${USERS}

OPTIONS_DEFINE=	OPENSSL UNRAR
OPTIONS_DEFAULT=	OPENSSL UNRAR

OPENSSL_RUN_DEPENDS=	${PYTHON_PKGNAMEPREFIX}openssl>0:${PORTSDIR}/security/py-openssl
UNRAR_RUN_DEPENDS=	unrar:${PORTSDIR}/archivers/unrar

.include <bsd.port.pre.mk>

do-install:
	${MKDIR} ${STAGEDIR}${DATADIR}/${GH_PROJECT}
	cd ${WRKSRC} && ${COPYTREE_SHARE} . ${STAGEDIR}${DATADIR}/${GH_PROJECT}

.include <bsd.port.post.mk>
