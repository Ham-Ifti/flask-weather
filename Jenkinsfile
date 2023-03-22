pipeline {
    agent any

    stages {
        // stage('Clone repository') {
        //     steps {
        //         git credentialsId: 'cred_github', url: 'https://github.com/Ham-Ifti/flask-weather'
        //     }
        // }
        
        stage('Build image') {
            steps {
                script {
                    dockerImage = docker.build("hamzaiftikhar/weather-app:latest")
                }
            }
        }
        
        stage('Push image') {
            steps {
                script {
                    withDockerRegistry([credentialsId: "dhub_iftikhar", url: ""]) {
                        dockerImage.push()
                    }
                }
            }
        }
        
        stage('Run image') {
            steps {
                sh 'docker stop weather-app || true'
                sh 'docker rm weather-app || true'
                sh 'docker run -d --name weather-app -p 5000:5000 hamzaiftikhar/weather-app:latest'
            }
        }
    }
}
