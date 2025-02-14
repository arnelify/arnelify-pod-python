# Server Makefile
# See https://www.gnu.org/software/make/manual/make.html for more about make.

# PYTHON
PYTHON = venv/bin/python
PYTHON_FLAGS = -m

# NUITKA
NUITKA = ../venv/bin/nuitka
NUITKA_FLAGS = --standalone --onefile --remove-output

# PATH
PATH_BUILD_BIN = server
PATH_BUILD_DIR = ../pod
PATH_BUILD_SRC = server.py
PATH_WATCH_SRC = watch

# BEFORE
BEFORE = clear

# SCRIPTS
build:
	${BEFORE} && ${NUITKA} ${NUITKA_FLAGS} --output-dir=${PATH_BUILD_DIR} --output-filename=${PATH_BUILD_BIN} ${PATH_BUILD_SRC}

watch:
	${BEFORE} && ${PYTHON} ${PYTHON_FLAGS} ${PATH_WATCH_SRC}