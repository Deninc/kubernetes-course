This project include exercise:
- 1.01
- 1.03
- 1.07
- 1.10
- 1.11

```bash
# inside folder generator
docker build -t thangnv2212/main-app-generator .
docker push thangnv2212/main-app-generator

# inside folder reader
docker build -t thangnv2212/main-app-reader .
docker push thangnv2212/main-app-reader

# make sure persitentvolume.yaml and persistentvolumeclaim.yaml are deployed, then:
kubectl apply -f manifests/deployment-persistent.yaml
kubectl apply -f manifests/service.yaml
kubectl apply -f manifests/ingress.yaml
```

Deployed to localhost:8081
