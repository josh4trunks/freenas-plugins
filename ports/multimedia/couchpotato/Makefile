# $FreeBSD$

PORTNAME=	couchpotato
PORTVERSION=	autoupdate.9
PORTREVISION=	5
CATEGORIES=	multimedia

MAINTAINER=	joshruehlig@gmail.com
COMMENT=	Automatic Movie Downloading via NZBs & Torrents

LICENSE=	GPLv3

RUN_DEPENDS=	${PYTHON_PKGNAMEPREFIX}sqlite3>0:${PORTSDIR}/databases/py-sqlite3 \
		${PYTHON_PKGNAMEPREFIX}lxml>0:${PORTSDIR}/devel/py-lxml

USES=	python:2.6-2.7

USE_GITHUB=     yes
GH_ACCOUNT=     CouchPotato
GH_PROJECT=     CouchPotatoServer
GH_COMMIT=      4476423
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
