pipeline {
    agent any

    
    stages{
        stage("git checkout"){
            steps{

            git branch: 'main', url: 'https://github.com/shubham-badade-ats/test.git'
            }
        }
        stage("run script"){
            steps{
                sh 'python script.py'


             
             
            }
           
        


   
    
}
}