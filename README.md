# Minikube Example Project

This project demonstrates the use of the following:

- minikube + docker
- flask
- dependency injection with IoC Container


## Instructions (Requires python 3.5+)

### Run the application outside of kubenertes (no docker)

1. Just run the flask app like any other python script. This requires that your build
environment and python environment are setup correctly (not ideal)
    - `pip install -r requirements.txt`
    - `python app/main.py`

### Run the application in docker (better way)

1. `docker build . -t mini-kube-example:latest`

2. `docker run --rm -p 8080:8080 mini-kube-example:latest`

### Run in local kubernetes cluster (best way)

1. make sure minikube and kubectl are installed, and kubectl context is pointing to `minikube`

2. make sure docker is installed

3. start minikube `minikube start`

4. run `./deploy.sh` which will build and deploy the docker image to the kube cluster

5. a link will be printed to the terminal once the deploy script is finished. 
open the link in web browser to view the application.

6. to delete the service and node(s), run `./undeploy.sh`
