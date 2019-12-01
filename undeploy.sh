#!/usr/bin/env bash

set -e

eval $(minikube docker-env)

app_name="mini-kube-example"

kubectl delete service ${app_name}

kubectl delete deployments ${app_name}

eval $(minikube docker-env -u)
