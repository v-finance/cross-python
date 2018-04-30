
Alternative scons based build script for the CPython interpreter.

The aspiration of this script is to have a modular and easy to customize
build script that facilitates cross compilation of the CPython interpreter.


Basic use
=========

Make sure scons is installed ::

    sudo apt-get install scons

Download and unzip the Python source code.

Start the build script by pointing it to the Python source code ::

    scons --srcdir=/path/to/Python-3.6.4
