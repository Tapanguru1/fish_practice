pipeline {
  agent any 
  stages {
   stage('Clone Source Repository') {
                /* Cloning the repository for web application */
                steps {
                    checkout scm
                }
            }
        stage('Verify The Clone') {
                steps{
                    sh 'ls'
                }
            }
            stage('Verify The Steps') {
                steps{
                    sh 'cat Jenkinsfile'
                }
            }
    stage('Build') {
      steps {
        sh "docker build -t fastapi:v1 ."
      }
    }
    stage('Run') {
      steps {
        sh "docker run -d -p 8008:8008 --name fastapiapp23 fastapi:v1"
      }
    }
     stage('Test') {
      steps {
        sh 'curl http://localhost:8008/'
      }
    }
  }
}
