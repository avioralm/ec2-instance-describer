# EC2 instances describer project

In this project we will run two pipelines in order to display running instances tagged with k8s tag name every 5 minutes.


## Installation:

1. Install jenkins on remote/local machine
2. Install the following plugins(along with suggested plugins installation):
- Amazon Web Services SDK
- Credentials Binding Plugin
- Docker Pipeline
3. Go to Manage Jenkins-> Manage Credentials -> And add credentials of kind AWS Credentials	and fill in your aws access and secret key 
4. Create two piplines: 
- CI Pipeline - Build python app using dockerfile
- Discarbe instances Pipeline - Run built docker image from last successfull build of CI pipline.

CI Pipeline (Jenkinsfile)

    - Pull from GitHub
    - Build Docker image: This stage builds a Docker image using the Docker plugin
   

Discarbe instances Pipeline (Jenkinsfile.run)

    - Configure jenkins job to run predicly:
      Go to the section of Build Triggers -> Build periodically and add */5 * * * *
    - Run Docker image: run last successfull build of ci pipeline

    

