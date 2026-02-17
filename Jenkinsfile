pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "kabubabu/scientific-calculator"
    }

    stages {

        stage('Install Dependencies') {
            steps {
                sh 'pip3 install -r requirements.txt || true'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'python3 -m unittest test_calculator.py'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $DOCKER_IMAGE:latest .'
            }
        }

        stage('Push Docker Image') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub-creds',
                                                  usernameVariable: 'USERNAME',
                                                  passwordVariable: 'PASSWORD')]) {
                    sh '''
                        echo $PASSWORD | docker login -u $USERNAME --password-stdin
                        docker push $DOCKER_IMAGE:latest
                    '''
                }
            }
        }
    }
}

