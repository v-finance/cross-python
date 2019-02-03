
Alternative meson based build script for the CPython interpreter.

The aspiration of this script is to have a modular and easy to customize
build script that facilitates cross compilation of the CPython interpreter.

Basic use
=========

Make sure meson is installed ::

    sudo apt-get install meson ninja-build

Download and unzip the Python source code.

Start the build script by pointing it to the Python source code ::

    meson builddir
    meson configure -Dsource=../cpython builddir
    ninja -C builddir

Terminology
===========

Meson definitions are the following:

 * build machine is the computer that is doing the actual compiling.

 * host machine is the machine on which the compiled binary will run.
 
 * target machine is the machine on which the compiled binary's output will run, only meaningful if the program produces machine-specific output.

Cross compiling
===============

 * binfmt-misc support running exe files under linux when wine is installed,
   it creates /proc/sys/fs/binfmt_misc/wine which allows the configure tests
   work.

 * the default configuration of wine should be changed to allow the CPython
   interpreter to start :

    * start `winecfg`
    * Go to the `Libraries` tab
    * Select `api-ms-win-core-path-xxx` in `New override for library`
    * Press `Add`
    * Select the library in `Existing overrides`, press `Edit`
    * Set the library to `disabled`
