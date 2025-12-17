pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Starting CI/CD pipeline'
            }
        }

        stage('Deploy with Docker Compose') {
            steps {
                sh 'docker-compose down || true'
                sh 'docker-compose up --build -d'
            }
        }
    }
}
