```bash
docker build -t thangnv2212/pong-app . && docker push thangnv2212/pong-app

kubectl apply -f manifests/sealedsecret.yaml
kubectl apply -f manifests/statefulset.yaml
kubectl apply -f manifests/deployment.yaml
```

Go to localhost:8081/pingpong
