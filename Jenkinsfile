pipeline {
    agent any

    stages {   
        stage('Build image') {
            dockerImage = docker.build("hamzaiftikhar/weather-app:latest")
        }
        
        stage('Push image') {
            withDockerRegistry([ credentialsId: "dhub_iftikhar", url: "" ]) {
                dockerImage.push()
            }
        }    

        stage('Run image') {
            sh 'docker stop weather-app || true'
            sh 'docker rm weather-app || true'
            sh 'docker run -d --name weather-app -p 5000:5000 hamzaiftikhar/weather-app:latest'
        }
    }
}