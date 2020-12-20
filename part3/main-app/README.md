```bash
docker build -t thangnv2212/main-app-generator generator && docker push thangnv2212/main-app-generator
docker build -t thangnv2212/main-app-reader reader && docker push thangnv2212/main-app-reader

# config map
kubectl create configmap dotenv-file \
       --from-env-file=configmap/dotenv.properties

kubectl apply -k
```

Go to localhost:8081
