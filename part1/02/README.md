```bash
docker build -t thangnv2212/1.02 .
docker push thangnv2212/1.02
kubectl create deployment 1.02-dep --image=thangnv2212/1.02
```
