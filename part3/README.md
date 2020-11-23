GKE cluster
```bash
gcloud container clusters create dwk-cluster --zone=europe-north1-b
gcloud container clusters get-credentials dwk-cluster --zone=europe-north1-b
```

Create namespace
```bash
brew install kubectx # helper tool kubens
kubectl create namespace main-ns
kubectl create namespace todo-ns
kubens main-ns
```
