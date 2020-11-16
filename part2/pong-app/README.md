This project include exercise:

```bash
docker build -t thangnv2212/pong-app . && docker push thangnv2212/pong-app

kubectl apply -f manifests/secret.yaml
kubectl apply -f manifests/deployment.yaml
kubectl apply -f manifests/statefulset.yaml
```

Deployed to localhost:8081/pingpong
