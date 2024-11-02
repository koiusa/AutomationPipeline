pipeline {
  agent {
    node {
      label 'worker'
    }
  }
  triggers {
    cron('*/10 * * * *')
  }
  stages {
    stage('Print') {
      steps {
        echo 'workerCache'
      }
    }

    stage('Activate') {
      steps {
        powershell 'python -m venv .'
        powershell 'Scripts\\activate'
        powershell 'python -m pip install --upgrade pip'
        powershell 'pip install -r requirements.txt'
      }
    }
    stage('Execute') {
      parallel {
        stage('worker') {
          steps {
            powershell 'python .\\worker\\main.py'
          }
        }
        stage('logs') {
          steps {
            powershell 'python .\\logs\\main.py'
          }
        }
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