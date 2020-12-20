```bash
docker build -t thangnv2212/main-app-generator generator && docker push thangnv2212/main-app-generator
docker build -t thangnv2212/main-app-reader reader && docker push thangnv2212/main-app-reader

# make sure persitentvolume.yaml and persistentvolumeclaim.yaml are deployed, then:
kubectl apply -f manifests/deployment-persistent.yaml
kubectl apply -f manifests/service.yaml
kubectl apply -f manifests/ingress.yaml
```

Go to to localhost:8081
