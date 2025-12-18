pipeline {
    agent any

    stages {

        stage('Checkout Code') {
            steps {
                echo 'Cloning repository from GitHub'
                git branch: 'main',
                    url: 'https://github.com/vibhakar246/flask-mysql-cicd-vibhakar246.git'
            }
        }

        stage('Build & Deploy with Docker Compose') {
            steps {
                echo 'Running docker compose'
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
