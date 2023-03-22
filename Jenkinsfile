node {   
    // stage('Clone repository') {
    //     git credentialsId: 'cred_github',
    //         url: 'https://github.com/Ham-Ifti/flask-weather'
    // }
    
    stage('Build image') {
       dockerImage = docker.build("hamzaiftikhar/weather-app:latest")
    }
    
    stage('Push image') {
        withDockerRegistry([ credentialsId: "dhub_iftikhar", url: "" ]) {
            dockerImage.push()
        }
    }    

    // stage('Run image') {
    //     docker.withRegistry('https://registry.hub.docker.com', 'cred_docker_hub') {
    //         def image = dockerImage.inside("--publish=5000:5000")  // maps container port 5000 to host port 5000
    //         {
    //             sh 'docker run -p 5000:5000 hmzakhalid/weather-app:latest'  // starts the container
    //         }
    //     }
    // }
}