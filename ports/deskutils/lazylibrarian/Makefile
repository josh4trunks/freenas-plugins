# $FreeBSD$

PORTNAME=	lazylibrarian
PORTVERSION=	1.0
CATEGORIES=	deskutils
MASTER_SITES=	GH

MAINTAINER=	joshruehlig@gmail.com
COMMENT=	An automated book downloader for SABnzbd.

LICENSE=	GPLv3 PSFL
LICENSE_COMB=	multi

RUN_DEPENDS=	${PYTHON_PKGNAMEPREFIX}sqlite3>0:${PORTSDIR}/databases/py-sqlite3

USE_PYTHON=	2.6+

USE_GITHUB=     yes
GH_ACCOUNT=     herman-rogers
GH_PROJECT=     LazyLibrarian-1
GH_COMMIT=      bf5db4f
GH_TAGNAME=     ${GH_COMMIT}

NO_BUILD=	yes
WRKSRC=		${WRKDIR}/${GH_ACCOUNT}-${GH_PROJECT}-${GH_COMMIT}
PLIST_SUB=	PORTNAME=${PORTNAME}
SUB_LIST+=	PORTNAME=${PORTNAME}
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
