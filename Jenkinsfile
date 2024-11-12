pipeline {
    agent any
    stages {
        stage('Clone Repo') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    // Build the Docker image
                    if (isUnix()) {
                        sh "docker build -t exampleapp:v35 ."
                    } else {
                        bat "docker build -t exampleapp:v35 ."
                    }
                }
            }
        }

        stage('Run Streamlit Application') {
            steps {
                script {
                    // Run the Docker container
                    if (isUnix()) {
                        sh "docker run -d -p 8501:8501 exampleapp:v35"
                    } else {
                        bat "docker run -d -p 8501:8501 exampleapp:v35"
                    }
                }
            }
        }
    }
}
