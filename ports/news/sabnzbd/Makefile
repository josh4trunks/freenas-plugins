# $FreeBSD$

PORTNAME=	sabnzbd
PORTVERSION=	0.7.20
CATEGORIES=	news
MASTER_SITES=	SF/${PORTNAME}plus/${PORTNAME}plus/${PORTVERSION}
DISTNAME=	SABnzbd-${PORTVERSION}-src

MAINTAINER=	joshruehlig@gmail.com
COMMENT=	A web-interface based binary newsgrabber in python, with nzb support

LICENSE=	BSD2CLAUSE BSD3CLAUSE GPLv2 GPLv3 ISCL MIT PSFL
LICENSE_COMB=	multi

RUN_DEPENDS=	${PYTHON_PKGNAMEPREFIX}cheetah>0:${PORTSDIR}/devel/py-cheetah \
		${PYTHON_PKGNAMEPREFIX}utils>0:${PORTSDIR}/devel/py-utils \
		${PYTHON_PKGNAMEPREFIX}sqlite3>0:${PORTSDIR}/databases/py-sqlite3

USES=		gettext python:2.5-2.7

NO_BUILD=	yes
WRKSRC=		${WRKDIR}/SABnzbd-${PORTVERSION}
PLIST_SUB=	PORTNAME=${PORTNAME} USER=${USERS} GROUP=${GROUPS}
SUB_LIST=	PORTNAME=${PORTNAME} USER=${USERS} GROUP=${GROUPS} PYTHON_CMD=${PYTHON_CMD}
SUB_FILES=	pkg-message
USE_RC_SUBR=	${PORTNAME}
CONFLICTS_INSTALL=	sabnzbdplus-*

PORTDOCS=	ABOUT.txt \
		CHANGELOG.txt \
		COPYRIGHT.txt \
		INSTALL.txt \
		ISSUES.txt \
		README.txt

USERS=		media
GROUPS=		${USERS}

OPTIONS_DEFINE=	PAR2CMDLINE UNRAR FEEDPARSER YENC OPENSSL
OPTIONS_DEFAULT=	PAR2CMDLINE UNRAR FEEDPARSER YENC OPENSSL
PAR2CMDLINE_DESC=	Required for postprocessing of par files
UNRAR_DESC=	Often required for unpacking many downloads
FEEDPARSER_DESC=	rss-feed support
YENC_DESC=	yenc support

PAR2CMDLINE_RUN_DEPENDS=	par2repair:${PORTSDIR}/archivers/par2cmdline-tbb
UNRAR_RUN_DEPENDS=	unrar:${PORTSDIR}/archivers/unrar
FEEDPARSER_RUN_DEPENDS=	${PYTHON_PKGNAMEPREFIX}feedparser>0:${PORTSDIR}/textproc/py-feedparser
YENC_RUN_DEPENDS=	${PYTHON_PKGNAMEPREFIX}yenc>0:${PORTSDIR}/news/py-yenc
OPENSSL_RUN_DEPENDS=	${PYTHON_PKGNAMEPREFIX}openssl>0:${PORTSDIR}/security/py-openssl

.include <bsd.port.pre.mk>

do-install:
	${INSTALL} -d ${STAGEDIR}${DATADIR}/SABnzbd
	cd ${WRKSRC} && ${COPYTREE_SHARE} . ${STAGEDIR}${DATADIR}/SABnzbd

.include <bsd.port.post.mk>
