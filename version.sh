#!/bin/bash
#
# to get the python version from configure.ac, first select
# the version string with sed and remove newlines with tr.
#
sed -n "s/^.*PYTHON_VERSION,\s*\(\S*\))$/\1/p" $1 | tr -d "\n"
