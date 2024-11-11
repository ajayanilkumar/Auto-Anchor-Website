pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'exampleapp:v18'
        REPO_URL = 'https://github.com/ajayanilkumar/Auto-Anchor-Website.git' // Replace with your GitHub repo URL
    }

    stages {
        stage('Checkout') {
            steps {
                // Checkout the GitHub repository
                git branch: 'main', url: env.REPO_URL
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    // Build the Docker image
                    sh "docker build -t ${DOCKER_IMAGE} ."
                }
            }
        }

        stage('Run Streamlit Application') {
            steps {
                script {
                    // Run the Docker container
                    sh "docker run -d -p 8501:8501 ${DOCKER_IMAGE}"
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
