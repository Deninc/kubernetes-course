```bash
docker build -t thangnv2212/todo-app .
docker push thangnv2212/todo-app
kubectl apply -f manifests/deployment.yaml
kubectl apply -f manifests/service.yaml
kubectl apply -f manifests/ingress.yaml
```

Go to localhost:8081, delete main-app ingress before running this.
