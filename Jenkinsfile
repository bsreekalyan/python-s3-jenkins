/* groovylint-disable LineLength */
/* groovylint-disable-next-line CompileStatic */
pipeline {
    agent any
    parameters {
        booleanParam(name: 'RELOAD_JOB', defaultValue: false, description: 'Reload job from Jenkinsfile and exit')
        string(name: 'PROJECTS', description: 'Enter Single/Multiple Project Names separated by comma delimiter. example: azure-data-warehouse,oracle')
        string(name: 'VERSION', defaultValue: '', description: 'Version number for the new release')
        string(name: 'RC_VERSION', defaultValue: '', description: 'Release candidate version from where to create the new version')
    }
    stages {
        stage('Reload pipeline from Jenkinsfile') {
            when {
                expression { return params.RELOAD_JOB == true }
            }
            steps {
                echo('Ended pipeline after reloading')
            }
        }
        stage('Copy the Release Candidate to final Directory in aws s3 bucket') {
            when {
                expression { params.RELOAD_JOB == false }
            }
            steps {
                sh """ #!/usr/bin/env bash
                set -eu
                export PROJECTS=$PROJECTS
                export VERSION=$VERSION
                export RC_VERSION=$RC_VERSION
                sh ./python_setup.sh
                python3 main.py
                """
            }
        }
    }
}
