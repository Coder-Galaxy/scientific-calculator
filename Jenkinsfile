pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                git 'https://github.com/Coder-Galaxy/scientific-calculator.git'
            }
        }

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
    }
}

