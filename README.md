# Envoy Proxy Examples
Examples of Envoy proxy

## Usage Tutorial
Deploy flask web microservice in Kubernetes: 
```bash
$ kubectl create configmap envoy-config --from-file flask-app-envoy/envoy.json
$ kubectl apply -f flask-app-envoy/deployment.yaml
$ kubectl apply -f flask-app-envoy/service.yaml
```
Deploy The Kubernetes Envoy Service Discovery Service:
```bash
$ git clone https://github.com/kelseyhightower/kubernetes-envoy-sds.git
$ cd kubernetes-envoy-sds
$ kubectl apply -f deployments/kubernetes-envoy-sds.yaml
$ kubectl apply -f services/kubernetes-envoy-sds.yaml
```
Deploy Edge Envoy:
```bash
$ kubectl create configmap edge-envoy-config --from-file edge-envoy/envoy.json
$ kubectl apply -f edge-envoy/deployment.yaml
$ kubectl apply -f edge-envoy/service.yaml
```
