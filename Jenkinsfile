@Library('jenkins-shared-lib') _
import org.example.Helper

node {
    properties([
        parameters([
            string(name: 'USERNAME', defaultValue: 'Mohamed', description: 'User Name'),
            choice(name: 'ACTION', choices: ['test', 'lint'], description: 'Action to perform')
        ])
    ])

    stage('Checkout') {
        checkout([$class: 'GitSCM',
            branches: [[name: '*/main']],
            userRemoteConfigs: [[
                url: 'https://github.com/MohamedOsama911/ITI_Python-CI_CD_Practice.git',
                credentialsId: 'github'
            ]]
        ])
    }

    stage('Install Dependencies') {
        sh 'pip install -r requirements.txt'
    }

    stage('Shared Lib Demo') {
        Helper.sayHello(params.USERNAME)
        def result = bounds(5, 10)
        echo "Bounds Result: ${result}"
    }

    stage('Run in Parallel') {
        parallel(
            "Run Tests": {
                if (params.ACTION == 'test') {
                    sh 'pytest tests/'
                }
            },
            "Lint": {
                if (params.ACTION == 'lint') {
                    sh 'echo "Pretend linting code..."'
                }
            }
        )
    }
}
