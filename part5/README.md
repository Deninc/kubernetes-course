Create cluster
```bash
k3d cluster create -p 8081:80@loadbalancer --agents 2
linkerd install | kubectl apply -f -
```
