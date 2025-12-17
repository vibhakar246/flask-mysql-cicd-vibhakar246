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
                sh '''
                cd flask-mysql-cicd-vibhakar246
                docker-compose down || true
                docker-compose up --build -d
                '''
            }
        }
    }
}
