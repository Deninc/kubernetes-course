```bash
docker build -t thangnv2212/pong-app .
docker push thangnv2212/pong-app

# make sure persitentvolume.yaml and persistentvolumeclaim.yaml are deployed, then:
kubectl apply -f manifests/deployment-persistent.yaml
kubectl apply -f manifests/service.yaml
kubectl apply -f manifests/ingress.yaml
```

Go to localhost:8081/pingpong
