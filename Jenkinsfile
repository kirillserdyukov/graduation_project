pipeline {
    agent { docker { image 'python:3.9.9-alpine' } }
    stages {
        stage('build') {
            steps {
                sh 'python --version'
            }
        }
    }
}