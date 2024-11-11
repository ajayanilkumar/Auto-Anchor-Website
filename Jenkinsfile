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
                    sh "docker build -t exampleapp:v18 ."
                }
            }
        }

        stage('Run Streamlit Application') {
            steps {
                script {
                    // Run the Docker container
                    sh "docker run -d -p 8501:8501 exampleapp:v35"
                }
            }
        }
    }
}
