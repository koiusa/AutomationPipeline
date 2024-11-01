pipeline {
  agent {
    node {
      label 'worker'
    }

  }
  stages {
    stage('Print') {
      steps {
        echo 'test'
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