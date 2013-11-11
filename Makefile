#
#	Makefile - wrap around create_plugin to make things simple
#
.include <bsd.own.mk>

TOP=	${.CURDIR}
PLUGINSDIR=	${TOP}/plugins
PLUGINS!=	ls ${PLUGINSDIR}
TARGETS=
CREATE_PLUGIN=	${TOP}/create_plugin

.for _p in ${PLUGINS}
TARGETS+=	${_p}
.endfor

.include <bsd.prog.mk>

.for _p in ${PLUGINS}
${_p}:
	@cd ${TOP}; ${CREATE_PLUGIN} ${.TARGET}
.endfor

list:
	@echo ${TARGETS}

help:
	@echo "------------------------------------------------------------"
	@echo "                   Available Targets                        "
	@echo "------------------------------------------------------------"
.for _p in ${PLUGINS}
	@printf "%-25s- build ${_p} plugin\n" "${_p}"
.endfor
	@printf "%-25s- list all targets\n" list
	@printf "%-25s- build all targets\n" all
	@echo "------------------------------------------------------------"

clean:
	rm -rf ${TOP}/build

# This is a dummy target for now - might do something useful later.
git-internal:
	@echo "Setting up for internal git repository"

# This is a dummy target for now - might do something useful later.
git-external:
	@echo "Setting up for external git repository"

all: ${PLUGINS}
