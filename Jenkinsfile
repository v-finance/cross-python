pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                sh 'git clean -dfx'
                sh 'git clone -b 3.8 --single-branch https://github.com/python/cpython.git cpython'
            }
        }
    }
}
