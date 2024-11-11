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
                    sh "sudo docker build -t exampleapp:v18 ."
                }
            }
        }

        stage('Run Streamlit Application') {
            steps {
                script {
                    // Run the Docker container
                    sh "sudo docker run -d -p 8501:8501 exampleapp:v18"
                }
            }
        }
    }

    post {
        always {
            echo "Pipeline finished."
        }
        cleanup {
            // Cleanup: Stop and remove any running containers with this image
            script {
                sh "docker ps -q --filter ancestor=${DOCKER_IMAGE} | xargs -r docker stop"
            }
        }
    }
}
