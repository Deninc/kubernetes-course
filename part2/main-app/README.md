```bash
# inside folder generator
docker build -t thangnv2212/main-app-generator . && docker push thangnv2212/main-app-generator

# inside folder reader
docker build -t thangnv2212/main-app-reader . && docker push thangnv2212/main-app-reader

# config map
kubectl create configmap dotenv-file \
       --from-env-file=configmap/dotenv.properties

kubectl apply -f manifests/deployment.yaml
```

Go to localhost:8081
