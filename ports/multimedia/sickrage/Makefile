# $FreeBSD$

PORTNAME=	sickrage
PORTVERSION=	9.3.3
CATEGORIES=	multimedia

MAINTAINER=	joshruehlig@gmail.com
COMMENT=	Video File Manager for TV Shows

LICENSE=	GPLv3 PSFL
LICENSE_COMB=	multi

RUN_DEPENDS=	${PYTHON_PKGNAMEPREFIX}cheetah>0:${PORTSDIR}/devel/py-cheetah \
		${PYTHON_PKGNAMEPREFIX}utils>0:${PORTSDIR}/devel/py-utils \
		${PYTHON_PKGNAMEPREFIX}sqlite3>0:${PORTSDIR}/databases/py-sqlite3 \
		${PYTHON_PKGNAMEPREFIX}imaging>0:${PORTSDIR}/graphics/py-imaging \
		${PYTHON_PKGNAMEPREFIX}lxml>0:${PORTSDIR}/devel/py-lxml

USES=	python:2.6-2.7

USE_GITHUB=     yes
GH_ACCOUNT=     SiCKRAGETV
GH_PROJECT=     SickRage
GH_COMMIT=      26a1aae
GH_TAGNAME=     ${GH_COMMIT}

NO_BUILD=	yes
PLIST_SUB=	PORTNAME=${PORTNAME} USER=${USERS} GROUP=${GROUPS}
SUB_LIST=	PORTNAME=${PORTNAME} USER=${USERS} GROUP=${GROUPS} PYTHON_CMD=${PYTHON_CMD}
SUB_FILES=	pkg-message
USE_RC_SUBR=	${PORTNAME}

USERS=		media
GROUPS=		${USERS}

OPTIONS_DEFINE=	OPENSSL UNRAR
OPTIONS_DEFAULT=	OPENSSL UNRAR

.include <bsd.port.pre.mk>

.if ${PORT_OPTIONS:MOPENSSL}
RUN_DEPENDS+=	${PYTHON_PKGNAMEPREFIX}openssl>0:${PORTSDIR}/security/py-openssl
.endif

.if ${PORT_OPTIONS:MUNRAR}
RUN_DEPENDS+=	unrar:${PORTSDIR}/archivers/unrar
.endif

do-install:
	${INSTALL} -d ${STAGEDIR}${DATADIR}/${GH_PROJECT}
	cd ${WRKSRC} && ${COPYTREE_SHARE} . ${STAGEDIR}${DATADIR}/${GH_PROJECT}

.include <bsd.port.post.mk>
