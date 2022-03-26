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

  }

}