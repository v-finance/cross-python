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
    }
}
