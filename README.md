# Envoy Proxy Examples
Examples of Envoy proxy

## Usage Tutorial
Deployment flask web microservice in Kubernetes: 
```bash
$ kubectl create configmap envoy-config --from-file flask-app-envoy/envoy.json
$ kubectl apply -f flask-app-envoy/deployment.yaml
$ kubectl apply -f flask-app-envoy/service.yaml
```
