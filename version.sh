#!/bin/bash
#
# to get the python version from configure.ac, first select
# the version string with sed and remove newlines with tr.
#
sed -n "s/^m4_define.*PYTHON_VERSION.*\([0-9]\+\.[0-9]\+\).*)$/\1/p" $1 | tr -d "\n"
