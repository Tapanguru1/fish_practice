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
        sh "docker run -d -p 8008:8008 tapan1"
      }
    }
     stage('Test') {
      steps {
        sh 'echo http://localhost:8008/'
      }
    }
  }
}
