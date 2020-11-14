This project include exercise:
- 2.01

```bash
# inside folder generator
docker build -t thangnv2212/main-app-generator . && docker push thangnv2212/main-app-generator

# inside folder reader
docker build -t thangnv2212/main-app-reader . && docker push thangnv2212/main-app-reader

kubectl apply -f manifests/deployment.yaml
kubectl apply -f manifests/service.yaml
kubectl apply -f manifests/ingress.yaml
```

Deployed to localhost:8081
