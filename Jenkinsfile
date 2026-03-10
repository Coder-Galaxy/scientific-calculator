pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "kabubabu/scientific-calculator"
    }

    stages {

        stage('Install Dependencies') {
            steps {
                sh 'pip3 install --break-system-packages -r requirements.txt || true'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'python3 -m unittest test_calculator.py'
            }
        }

        stage('Docker Login') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub-creds',
                    usernameVariable: 'USERNAME',
                    passwordVariable: 'PASSWORD'
                )]) {
                    sh '''
                        echo $PASSWORD | docker login -u $USERNAME --password-stdin
                    '''
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $DOCKER_IMAGE:latest .'
            }
        }

        stage('Push Docker Image') {
            steps {
                sh 'docker push $DOCKER_IMAGE:latest'
            }
        }

        stage('Deploy with Ansible') {
            steps {
                sh 'ansible-playbook -i inventory deploy.yml'
            }
        }
    }

    post {

        success {
            mail to: 'piyushsinghcu@gmail.com',
                 subject: "SUCCESS: Jenkins Build #${env.BUILD_NUMBER}",
                 body: """
Build SUCCESSFUL!

Project: Scientific Calculator CI/CD Pipeline
Job Name: ${env.JOB_NAME}
Build Number: ${env.BUILD_NUMBER}
Build URL: ${env.BUILD_URL}

Docker image built and deployed successfully.
"""
            echo 'Pipeline completed successfully 🚀'
        }

        failure {
            mail to: 'piyushsinghcu@gmail.com',
                 subject: "FAILED: Jenkins Build #${env.BUILD_NUMBER}",
                 body: """
Build FAILED!

Project: Scientific Calculator CI/CD Pipeline
Job Name: ${env.JOB_NAME}
Build Number: ${env.BUILD_NUMBER}
Build URL: ${env.BUILD_URL}

Please check Jenkins console logs.
"""
            echo 'Pipeline failed ❌'
        }

        always {
            sh 'docker logout || true'
        }
    }
}