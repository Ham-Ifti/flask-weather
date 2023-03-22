pipeline {
    agent any
    
    stages {
        stage("Build Docker Image") {
            steps {
                sh """
                apt-get update
                apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
                docker run hello-world
                """
            }
        }
    }
}