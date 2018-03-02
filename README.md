# pwgen-ws

This is my attempt to create a microservice in python. This microservice is very simple, and is a proof of concept for "how to use K8S / Prometheus" in a CI/CD context.

# Requirements
* A working K8S cluster (or minikube)
* A Drone-CI CI/CD setup
* A working Prometheus setup
* A oAuth2 external service for authorisation (wishlist)

# Drone configuration
```
$ export DRONE_SERVER="https://drone.example.com"
$ export DRONE_TOKEN="qjSDi2lj19Lk6QZC046HzLRBsDfPVDjqpZqj3G60cbRJe06hYijeZNZzpkVelGj2W6DRrw4dKGj62uWVI4lMTEihuAkdfFne0TcYmfCwh8RcaREmNiU3s6jyCyk3aopS"
```

# Drone pipeline configuration
```
# Dockerhub credentials
$ drone secret add pgauthier/pwgen-ws DOCKER_USERNAME myusername
$ drone secret add pgauthier/pwgen-ws DOCKER_PASSWORD mypassword
 
# Kubernetes credentials
$ drone secret add --image=pgauthier2/drone-helm pgauthier/pwgen-ws DEV_API_SERVER https://my-k8s-cluster.example.com
$ drone secret add --image=pgauthier2/drone-helm pgauthier/pwgen-ws DEV_KUBERNETES_TOKEN 7seRy5jxZx6N7GH0IaSuLOBI9AEImSLdQmdGayiyYGBNY32DTkm02mCCgaoGxlSr4EnyPM8CZ8rGO4URCBRshj02w2UukRgpOTwn5C0Cnmh8jqf0a32awBz2jhRJaIhU
 
# Helm configuration
# Base64 encoded
$ drone secret add pgauthier/widget-launcher DEV_DOCKERCFG KbhHUcM0NjEyEiBdf9MaKCVl70Tp0DZ5DjgIAXjmwuZoQKVVTXpEwQNm7UOgpNQq
```

# Information about the structure of the project
* Charts directory contain the k8s definition, in the helm packaging format (https://github.com/kubernetes/helm)
* .dockerignore
* .drone.yml
* .drone.yml.sig
* Dockerfile
* README.md
* requirements.txt