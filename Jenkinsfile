pipeline {
    agent {
        docker {
            image 'python:3.12-slim'
            args '-u root:root -v $HOME/.cache/pip:/root/.cache/pip'
        }
    }

    environment {
        PIP_DISABLE_PIP_VERSION_CHECK = '1'
        PYTHONUNBUFFERED = '1'
    }

    options {
        timestamps()
        ansiColor('xterm')
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install dependencies') {
            steps {
                sh '''
                    set -eux
                    python -m pip install --upgrade pip
                    pip install -r requirement.txt
                    playwright install --with-deps chromium
                '''
            }
        }

        stage('Run pytest-bdd suite') {
            steps {
                sh '''
                    set -eux
                    mkdir -p report
                    pytest -v --html=report/report.html --self-contained-html
                '''
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: 'report/**/*', allowEmptyArchive: true
        }
    }
}

