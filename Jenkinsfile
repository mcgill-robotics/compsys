pipeline {
  agent any
  stages {
    stage('Shellcheck') {
      parallel {
        stage('install') {
          steps {
            sh 'shellcheck --version'
            sh 'shellcheck install'
          }
        }
        stage('update') {
          steps {
            sh 'shellcheck --version'
            sh 'shellcheck update'
          }
        }
        stage('roboticrc') {
          steps {
            sh 'shellcheck --version'
            sh 'shellcheck -s bash roboticrc'
            sh 'shellcheck -s bash aliases'
          }
        }
        stage('setup/config') {
          steps {
            sh 'shellcheck --version'
            sh 'shellcheck setup/config/install'
            sh 'shellcheck -s bash --exclude=SC1090 setup/config/rc'
          }
        }
        stage('setup/ros') {
          steps {
            sh 'shellcheck --version'
            sh 'shellcheck setup/ros/install'
          }
        }
        stage('setup/zsh') {
          steps {
            sh 'shellcheck --version'
            sh 'shellcheck setup/zsh/install'
            sh 'shellcheck -s bash --exclude=SC1090 setup/zsh/zshrc'
          }
        }
      }
    }
    stage('YAPF') {
      steps {
        sh 'yapf --version'
        sh '[ -z "$(yapf --recursive --parallel --diff .)" ]'
      }
    }
  }
}
