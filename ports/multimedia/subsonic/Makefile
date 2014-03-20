# $FreeBSD$

PORTNAME=	subsonic
PORTVERSION=	4.9
CATEGORIES=	multimedia
MASTER_SITES=	SF
DISTNAME=	${PORTNAME}-${PORTVERSION}-standalone

MAINTAINER=	joshruehlig@gmail.com
COMMENT=	Subsonic streaming media server

LICENSE=	GPLv3

USE_JAVA=	yes
JAVA_VERSION=	1.6+
JAVA_RUN=	yes

NO_WRKSUBDIR=	yes
NO_BUILD=	yes
PLIST_SUB=	PORTNAME=${PORTNAME} USER=${USERS} GROUP=${GROUPS}
SUB_LIST=	PORTNAME=${PORTNAME} USER=${USERS} GROUP=${GROUPS} JAVA_CMD=${JAVA}
SUB_FILES=	pkg-message
USE_RC_SUBR=	${PORTNAME}

USERS=		media
GROUPS=		${USERS}

OPTIONS_DEFINE=	TRANSCODING
TRANSCODING_DESC=	Transcoding with FFmpeg
OPTIONS_DEFAULT=	TRANSCODING

.include <bsd.port.pre.mk>

.if ${PORT_OPTIONS:MTRANSCODING}
RUN_DEPENDS=	ffmpeg:${PORTSDIR}/multimedia/ffmpeg
PLIST_SUB+=	TRANSCODING=""
.else
PLIST_SUB+=	TRANSCODING="@comment "
.endif

do-install:
	${INSTALL} -d ${STAGEDIR}${DATADIR}/Subsonic ${STAGEDIR}/${ETCDIR}
	${INSTALL_DATA} ${WRKSRC}/subsonic.war ${STAGEDIR}${DATADIR}/Subsonic
	${INSTALL_DATA} ${WRKSRC}/subsonic-booter-jar-with-dependencies.jar ${STAGEDIR}${DATADIR}/Subsonic
	${INSTALL} ${WRKSRC}/config.ini.sample ${STAGEDIR}/${ETCDIR}
.if ${PORT_OPTIONS:MTRANSCODING}
	${INSTALL} -d ${STAGEDIR}/${ETCDIR}/transcode
	${LN} -sf ${PREFIX}/bin/ffmpeg ${STAGEDIR}/${ETCDIR}/transcode/ffmpeg
.endif

.include <bsd.port.post.mk>
