#!/usr/bin/env bash

set -e

eval $(minikube docker-env)

app_name="mini-kube-example"

docker build . -t ${app_name}:latest && \

kubectl run ${app_name} --image=${app_name}:latest --port=8080 --image-pull-policy=Never && \

kubectl expose deployment ${app_name} --type="LoadBalancer"

minikube service ${app_name} --url

