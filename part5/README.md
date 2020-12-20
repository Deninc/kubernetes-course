```bash
k3d cluster create --agents 2

docker build -t thangnv2212/dummysite-controller controller && docker push thangnv2212/dummysite-controller

kubectl apply -k .

kubectl port-forward <pod_name> 8080:80
```

Deploy static html to localhost:8080
