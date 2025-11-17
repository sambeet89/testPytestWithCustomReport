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

        stage('Build and Test') {
            steps {
                sh '''
                    set -eux
                    
                    # Determine correct requirements file
                    req_file=""
                    if [ -f requirement.txt ]; then
                        req_file="requirement.txt"
                    elif [ -f requirements.txt ]; then
                        req_file="requirements.txt"
                    else
                        echo "No requirement.txt or requirements.txt found in $PWD"
                        exit 1
                    fi
                    
                    python3 -m venv .venv
                    . .venv/bin/activate
                    python -m pip install --upgrade pip
                    pip install -r "$req_file"
                    playwright install --with-deps chromium
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
