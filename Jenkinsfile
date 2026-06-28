pipeline {
    agent any

    environment {
        IMAGE_NAME = "ticket-booking-app"
    }

    stages {

        stage('Clone Code') {
            steps {
                git 'https://github.com/Abhishek2003-boot/Ticket_booking'
            }
        }

        stage('SonarQube Scan') {
            steps {
                sh '''
                sonar-scanner \
                -Dsonar.projectKey=ticket-booking \
                -Dsonar.sources=. \
                -Dsonar.host.url=http://your-sonarqube-ip:9000 \
                -Dsonar.login=your-token
                '''
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $IMAGE_NAME:v1 .'
            }
        }

        stage('Push Docker Image to Nexus') {
            steps {
                sh '''
                docker tag $IMAGE_NAME:v1 your-nexus-ip:8082/$IMAGE_NAME:v1
                docker push your-nexus-ip:8082/$IMAGE_NAME:v1
                '''
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                sh 'kubectl apply -f deployment.yaml'
            }
        }
    }
}