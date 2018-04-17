pipeline {
  agent any
  stages {
    stage('Sanity Check') {
      parallel {
        stage('install') {
          steps {
            sh 'shellcheck --version'
            sh 'shellcheck --exclude=SC1091 install'
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
            sh 'shellcheck -s bash --exclude=SC1090,SC2164 roboticrc'
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
  }
}
