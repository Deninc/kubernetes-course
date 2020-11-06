This project include exercise:
- 1.02
- 1.04
- 1.05
- 1.06
- 1.08

```bash
docker build -t thangnv2212/todo-app .
docker push thangnv2212/todo-app
kubectl apply -f manifests/deployment.yaml
kubectl apply -f manifests/service.yaml
kubectl apply -f manifests/ingress.yaml
```
