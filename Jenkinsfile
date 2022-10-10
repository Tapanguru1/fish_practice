pipeline {
  agent any 
  stages {
    stage('Build') {
      steps {
        sh "docker build -t tapan1 ."
      }
    }
    stage('Run') {
      steps {
        sh "docker run -d -p 8080:8080 tapan1"
      }
    }
     stage('Test') {
      steps {
        sh 'curl http://localhost:8080/'
      }
    }
  }
}
