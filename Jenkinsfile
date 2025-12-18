pipeline {
    agent any

    stages {

        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }

        stage('Build & Deploy with Docker Compose') {
            steps {
                sh '''
                docker compose down || true
                docker compose up --build -d
                '''
            }
        }
    }

    post {
        success {
            echo 'Deployment completed successfully'
        }
        failure {
            echo 'Deployment failed'
        }
    }
}

