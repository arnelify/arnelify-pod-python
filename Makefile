# Boot Makefile
# See https://www.gnu.org/software/make/manual/make.html for more about make.

# PYTHON
PYTHON = venv/bin/python
PYTHON_FLAGS = -m

# PATH
PATH_SRC = src.core.boot.index

# BEFORE
BEFORE = clear

# SCRIPTS
setup:
	${BEFORE} && ${PYTHON} ${PYTHON_FLAGS} ${PATH_SRC} setup

build:
	${BEFORE} && ${PYTHON} ${PYTHON_FLAGS} ${PATH_SRC} build

watch:
	${BEFORE} && ${PYTHON} ${PYTHON_FLAGS} ${PATH_SRC} watch

migrate:
	${BEFORE} && ${PYTHON} ${PYTHON_FLAGS} ${PATH_SRC} migrate

seed:
	${BEFORE} && ${PYTHON} ${PYTHON_FLAGS} ${PATH_SRC} seed