pipeline {
    agent any
    stages {
        stage('Download Code') {
            steps {
                echo 'Getting latest code from GitHub...'
            }
        }
        stage('Test Code') {
            steps {
                echo 'Running Python app...'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying app to GCP...'
            }
        }
    }
}
