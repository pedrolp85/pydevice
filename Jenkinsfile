pipeline {

  agent any

  environment {
      MY_NAME = "Pedro"
  }


  stages {

    stage('Hello') {
        parallel {
            stage("1") {
                steps {
                    sh '''
                    echo "hola $MY_NAME"
                    '''
                }
            }
            stage("2") {
                steps {
                    sh '''
                    echo "hola David"
                    '''
                }
            }
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