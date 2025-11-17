pipeline {
    agent any

    environment {
        PIP_DISABLE_PIP_VERSION_CHECK = '1'
        PYTHONUNBUFFERED = '1'
    }

    options {
        timestamps()
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build and Test in Docker') {
            steps {
                sh '''
                    set -eux
                    docker run --rm \
                        -v "$PWD":/workspace \
                        -w /workspace \
                        -v "$HOME/.cache/pip":/root/.cache/pip \
                        python:3.12-slim \
                        bash -c "
                            set -eux
                            python -m pip install --upgrade pip
                            pip install -r requirement.txt
                            playwright install --with-deps chromium
                            mkdir -p report
                            pytest -v --html=report/report.html --self-contained-html
                        "
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

