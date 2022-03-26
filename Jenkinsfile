pipeline {

  agent any

  environment {
      MY_NAME = "Pedro"
  }


  stages {

    stage('Hello') {
      steps {
        sh '''
          echo "hola $MY_NAME"
        '''
      }
    }
    stage('Bye bye') {
      steps {
        sh '''
          echo "adios $MY_NAME"
        '''
      }
    }

  }

}