pipeline {
    agent any

    environment {
        AWS_REGION = 'us-west-2'  // Replace with your region
        S3_BUCKET = 'your-s3-bucket-name'  // Replace with your S3 bucket name
        CODEDEPLOY_APPLICATION = 'your-codedeploy-application'  // Replace with your CodeDeploy application name
        CODEDEPLOY_DEPLOYMENT_GROUP = 'your-deployment-group'  // Replace with your CodeDeploy deployment group name
    }

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/your-repository/simple-web-server.git'
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
