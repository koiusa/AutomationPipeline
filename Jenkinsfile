pipeline {
  agent {
    node {
      label 'primary'
    }

  }
  stages {
    stage('Print') {
      steps {
        echo 'test'
      }
    }

    stage('Activate') {
      steps {
        powershell 'py -m venv .'
        powershell 'Scripts\\activate'
      }
    }
    
    stage('Execute') {
      steps {
        powershell 'cd .\\worker'
        powershell 'py .\\main.py'
      }
    }

    stage('DeActivate') {
      steps {
        powershell 'deactivate'
      }
    }

  }
  post {
    failure {
      discordSend(description: BUILD_RESULT, footer: currentBuild.currentResult, webhookURL: WEBHOOK, successful: false)
    }

    success {
      discordSend(description: BUILD_RESULT, footer: currentBuild.currentResult, webhookURL: WEBHOOK, successful: true)
    }

  }
}