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

    stage('Activate') {
      steps {
        sh '''python -m venv .
py Scripts\\activate'''
      }
    }

    stage('DeActivate') {
      steps {
        sh 'deactivate'
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