pipeline {
    agent any
    stages {
        
        stage("Dockerfile lint") {
            agent {
                docker {
                    image "docker.io/hadolint/hadolint"
                    reuseNode true
                }                
            }
            steps {
                sh label: 'hadolint Dockerfile check', script: 'hadolint Dockerfile > hadolint-result.log'
            }
        }
        
        stage("Build image") {
            steps {
                script {
                    myapp = docker.build("vishnusk/py-demo:v${env.BUILD_ID}")
                }
            }
        }
        stage("Push image") {
            steps {
                script {
                    docker.withRegistry('https://registry.hub.docker.com', 'dockerid') {
                            myapp.push("latest")
                            myapp.push("v${env.BUILD_ID}")
                    }
                }
            }
        }        
        stage('Deploy to GKE') {
            steps{
                sh 'kubectl apply -f deployment.yaml'
                sh 'kubectl apply -f services.yaml'
            }
        }
        stage("Get frontend service") {
            steps {
                sleep(50) 
                sh 'kubectl get svc'
                sh 'kubectl get pods'
            }
        }
        stage("clean up") {
            steps {
                sleep(30) 
                sh 'kubectl delete deployment flask-app'
                sh 'kubectl delete svc flask-service'
            }
        }
    }    
    
    post {
        always {
            archiveArtifacts artifacts: '*-result.log', followSymlinks: false 
        }
    }
}
