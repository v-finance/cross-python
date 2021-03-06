pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                sh 'git clean -dfx -f'
                sh 'git clone -b 3.8 --single-branch https://github.com/python/cpython.git cpython'
            }
        }
        stage('Native build') {
            steps {
                sh 'meson -Dsource=cpython builddir-x86_64-redhat-linux --prefix="${PWD}/x86_64-redhat-linux"'
                sh 'ninja -C builddir-x86_64-redhat-linux'
            }
        }
        stage('Native install') {
            steps {
                sh 'ninja -C builddir-x86_64-redhat-linux install'
            }
        }
        stage('Native test') {
            steps {
                sh './x86_64-redhat-linux/bin/python -m test test_float'
            }
        }
        stage('Win64 build') {
            steps {
                sh 'meson -Dsource=cpython --cross-file cross-files/x86_64-w64-mingw32.txt --prefix="${PWD}/x86_64-w64-mingw32" builddir-x86_64-w64-mingw32'
                sh 'ninja -C builddir-x86_64-w64-mingw32'
            }
        }
        stage('Win64 install') {
            steps {
                sh 'ninja -C builddir-x86_64-w64-mingw32 install'
                sh 'cp /usr/x86_64-w64-mingw32/sys-root/mingw/bin/*.dll ./x86_64-w64-mingw32/bin/'
            }
        }
        stage('Win64 test') {
            steps {
                sh 'mkdir wine-prefix'
                sh 'wine --version'
                sh 'export WINEDLLOVERRIDES="mscoree,mshtml=" && export WINEPREFIX="${PWD}/wine-prefix" && export DISPLAY=:1 && wineconsole test_win64.bat'
                sh 'cat x86_64-w64-mingw32/bin/test.out'
            }
        }
        stage('Win32 build') {
            steps {
                sh 'meson -Dsource=cpython --cross-file cross-files/i686-w64-mingw32.txt --prefix="${PWD}/i686-w64-mingw32" builddir-i686-w64-mingw32'
                sh 'ninja -C builddir-i686-w64-mingw32'
            }
        }
        stage('Win32 install') {
            steps {
                sh 'ninja -C builddir-i686-w64-mingw32 install'
                sh 'cp /usr/i686-w64-mingw32/sys-root/mingw/bin/*.dll ./i686-w64-mingw32/bin/'
            }
        }
    }
}

