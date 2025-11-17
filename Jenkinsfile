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
                    req_file=""
                    if [ -f requirement.txt ]; then
                        req_file="requirement.txt"
                    elif [ -f requirements.txt ]; then
                        req_file="requirements.txt"
                    else
                        echo "No requirement.txt or requirements.txt found in $PWD"
                        exit 1
                    fi

                    docker run --rm \
                        -v "$PWD":/workspace \
                        -w /workspace \
                        -e REQ_FILE="$req_file" \
                        python:3.12-slim \
                        bash -c '
                            set -eux
                            : "${REQ_FILE:?Expected requirements file name passed in REQ_FILE}"
                            if [ ! -f "$REQ_FILE" ]; then
                                echo "Expected requirements file $REQ_FILE not found inside container"
                                exit 1
                            fi
                            python -m pip install --upgrade pip
                            pip install -r "$REQ_FILE"
                            playwright install --with-deps chromium
                            mkdir -p report
                            pytest -v --html=report/report.html --self-contained-html
                        '
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
