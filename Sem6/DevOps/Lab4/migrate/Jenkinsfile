pipeline {
    agent any
    
    stages {
        stage('Build and Run') {
            steps {
                sh '''
                cd /home/ifsvivek/code/Lab/Sem6/DevOps/Lab4/migrate
                ./gradlew run
                '''
            }
        }
    }
}