pipeline {
    agent any
    
    stages {
        stage("Build Docker Image") {
            steps {
                sh """
                sudo apt-get update
                sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
                sudo docker run hello-world
                """
            }
        }
    }
}