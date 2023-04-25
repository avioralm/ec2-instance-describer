pipeline {
  agent any

  stages {
    stage('Git Clone') {
      steps {
        cleanWs()
        git branch: 'main', url: 'https://github.com/avioralm/ec2-instance-describer.git'
      }
    }

    stage('Docker Build') {
      steps {
        script {
          docker.build("ec2-instance-describer:${env.BUILD_NUMBER}")
        }
      }
    }
  }
}
