This project include exercise:
- 1.01
- 1.03
- 1.07
- 1.10

```bash
docker build -t thangnv2212/main-app-generator .
docker push thangnv2212/main-app-generator

docker build -t thangnv2212/main-app-reader .
docker push thangnv2212/main-app-reader

kubectl apply -f manifests/deployment.yaml
kubectl apply -f manifests/service.yaml
kubectl apply -f manifests/ingress.yaml
```
