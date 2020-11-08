This project include exercise:
- 1.09
- 1.11

```bash
docker build -t thangnv2212/pong-app .
docker push thangnv2212/pong-app
kubectl apply -f manifests/deployment.yaml
kubectl apply -f manifests/service.yaml
kubectl apply -f manifests/ingress.yaml
```
