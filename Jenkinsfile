pipeline {
    agent any

    
    stages{
        stage("git checkout"){
            steps{

            git branch: 'main', url: 'https://github.com/shubham-badade-ats/test.git'
            }
        }
        stage("docker image"){
            steps{
             
             dir('/test') {


           script {
                    // Use a Docker image with necessary build tools
                    docker.image('docker:latest').inside {
                        // Build your application (replace with actual build command)
                        sh 'sudo docker build -t test:latest .'

                        // Push the Docker image to a registry
                        // sh "docker tag $IMAGE_NAME:$IMAGE_TAG $DOCKER_REGISTRY/$IMAGE_NAME:$IMAGE_TAG"
                        // sh "docker push $DOCKER_REGISTRY/$IMAGE_NAME:$IMAGE_TAG"
                    }
                }
            
       }
            }
           
        }
        stage("docker login"){
            steps{
            sh "docker login -u shubhambadade07 -p Pass@12345"
            }
            
        }
        stage("docker push shubhambadade07/test1:latest"){
            steps{
            sh "docker push shubhambadade07/test1:latest"
            }
        }


   
    
}
}