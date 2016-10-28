# $FreeBSD$

PORTNAME=	sickbeard
PORTVERSION=	9.3.1
CATEGORIES=	multimedia

MAINTAINER=	joshruehlig@gmail.com
COMMENT=	PVR & episode guide that downloads and manages all your TV shows

LICENSE=	GPLv3

RUN_DEPENDS=	${PYTHON_PKGNAMEPREFIX}cheetah>0:${PORTSDIR}/devel/py-cheetah \
		${PYTHON_PKGNAMEPREFIX}utils>0:${PORTSDIR}/devel/py-utils \
		${PYTHON_PKGNAMEPREFIX}sqlite3>0:${PORTSDIR}/databases/py-sqlite3 \
		${PYTHON_PKGNAMEPREFIX}imaging>0:${PORTSDIR}/graphics/py-imaging

USES=	python:2.5-2.7

USE_GITHUB=     yes
GH_ACCOUNT=     midgetspy  
GH_PROJECT=     Sick-Beard
GH_COMMIT=      7cfff7f
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
