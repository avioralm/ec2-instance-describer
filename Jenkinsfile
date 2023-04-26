pipeline {
  agent any

  stages {
    stage('Git Clone') {
      steps {
        git branch: 'main', url: 'https://github.com/avioralm/ec2-instance-describer.git'
      }
    }

    stage('Docker Build') {
      steps {
        script {
            try {
              docker.build("ec2-instance-describer:${env.BUILD_NUMBER}")
            } catch (err) {
                 echo "Error: ${err}"
                 currentBuild.result = 'FAILURE'
                 error "Failed to build Docker image"
             }

        }
      }
    }
  }

  post {
        always {
            cleanWs()
        }
    }
}