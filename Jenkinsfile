pipeline {
  agent any 
  stages {
    stage('Build') {
      steps {
        sh "docker build tapan1 ."
      }
    }
    stage('Run') {
      steps {
        sh "docker run -d -p 8008:8008 tapan1"
      }
    }
     stage('Test') {
      steps {
        sh 'curl http://localhost:8008/'
      }
    }
