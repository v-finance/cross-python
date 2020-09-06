
Alternative meson based build script for the CPython interpreter.

The aspiration of this script is to have a modular and easy to customize
build script that facilitates cross compilation of the CPython interpreter.

# Basic use

Make sure meson is installed :

```
    sudo dnf install meson ninja-build
```

Download and unzip the Python source code.

Start the build script by pointing it to the Python source code :

```
    meson -Dsource=../cpython builddir
    ninja -C builddir
```

In the example above it is assumed the CPython source code is checked out in `../cpython`.

# Terminology

Meson definitions are the following :

 - build machine is the computer that is doing the actual compiling.

 - host machine is the machine on which the compiled binary will run.
 
 - target machine is the machine on which the compiled binary's output will run.
   Only meaningful if the program produces machine-specific output.

# Cross compiling

Different configuration files for cross compiling are in the *cross-files* directory 

## Windows (mingw)

 - binfmt-misc: allows running .exe files under linux if wine is installed.
   It creates /proc/sys/fs/binfmt_misc/wine which allows the configure tests to
   work. On Debian there's the package `wine-binfmt`. On other distros you can
   do `echo ':DOSWin:M::MZ::/usr/bin/wine:' > /proc/sys/fs/binfmt_misc/register.`
   (run as root).

 - https://tecadmin.net/steps-install-wine-centos-rhel-fedora-systems/

 - the default configuration of wine might need to be changed to allow the CPython
   interpreter to start :

    - start `winecfg`
    - Go to the `Libraries` tab
    - Select `api-ms-win-core-path-<WHATEVER>` from the menu in `New override for library`
    - Press `Add`
    - Select the library in `Existing overrides`, press `Edit`
    - Set the library to `disabled`

Start the build script by using a cross-file:

```
    meson -Dsource=../cpython --cross-file cross-files/x86_64-w64-mingw32.txt --prefix="${PWD}/x86_64-w64-mingw32" builddir-x86_64-w64-mingw32
    ninja -C builddir-x86_64-w64-mingw32
    ninja -C builddir-x86_64-w64-mingw32 install
```

Note that `install` doesn't install it to the system, only locally reorganize the files into a working tree.
To run the Python for Windows build, the mingw runtime library and dependencies need to be available on the path:

```
    cd x86_64-w64-mingw32/bin
    export WINEPATH=/usr/x86_64-w64-mingw32/sys-root/mingw/bin/
    ./python.exe
```

# License

...

### Related

https://mingwpy.github.io/motivation.html

https://github.com/numpy/numpy/wiki/Numerical-software-on-Windows
