```bash
docker build -t thangnv2212/1.01 .
docker push thangnv2212/1.01
kubectl apply -f manifests/deployment.yaml
kubectl logs -f --tail=10 main-dep-6f786cc568-sjj5p
```
