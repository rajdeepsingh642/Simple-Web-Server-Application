pipeline {
    agent any

    environment {
        AWS_REGION = 'ap-south-1'  // Replace with your region
        S3_BUCKET = 'web-server74'  // Replace with your S3 bucket name
        CODEDEPLOY_APPLICATION = 'web-server'  // Replace with your CodeDeploy application name
        CODEDEPLOY_DEPLOYMENT_GROUP = 'web-server-app'  // Replace with your CodeDeploy deployment group name
    }

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/rajdeepsingh642/Simple-Web-Server-Application.git'
            }
        }

        stage('Package') {
            steps {
                sh 'zip -r simple-web-server.zip *'
            }
        }

        stage('Upload to S3') {
            steps {
                withAWS(region: "${AWS_REGION}", credentials: 'aws-credentials-id') {
                    s3Upload(bucket: "${S3_BUCKET}", file: 'simple-web-server.zip', path: 'deployments/simple-web-server.zip')
                }
            }
        }

        stage('Deploy with CodeDeploy') {
            steps {
                withAWS(region: "${AWS_REGION}", credentials: 'aws-credentials-id') {
                    sh """
                    aws deploy create-deployment \\
                        --application-name ${CODEDEPLOY_APPLICATION} \\
                        --deployment-group-name ${CODEDEPLOY_DEPLOYMENT_GROUP} \\
                        --s3-location bucket=${S3_BUCKET},bundleType=zip,key=deployments/simple-web-server.zip \\
                        --deployment-config-name CodeDeployDefault.OneAtATime
                    """
                }
            }
        }
    }
}
