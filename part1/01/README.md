```bash
docker build -t thangnv2212/1.01 .
docker push thangnv2212/1.01
kubectl create deployment 1.01-dep --image=thangnv2212/1.01
```
