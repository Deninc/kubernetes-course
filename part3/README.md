GKE cluster
```bash
gcloud container clusters create dwk-cluster --zone=europe-north1-b
gcloud container clusters get-credentials dwk-cluster --zone=europe-north1-b
```

Install sealed secrets
```bash
brew install kubeseal
kubectl apply -f https://github.com/bitnami-labs/sealed-secrets/releases/download/v0.12.1/controller.yaml
# for all secrets in all projects
kubeseal -o yaml < secret.yaml > sealedsecret.yaml
```

Create namespace
```bash
brew install kubectx # helper tool kubens
kubectl create namespace main-ns
kubectl create namespace todo-ns
kubens main-ns
```

### Exercise 3.06: DBaaS vs DIY

|  | Google Cloud SQL | Postgres on GKE |
|-|-|-|
| Initialization | Easy interface to interact | High learning curve of configuring SatefulSets |
| Maintanence (patching, scaling) | Automatically | Can be done but manually |
| Backups/Replication/Failover | Automatically | Data loss might happen because pods are mortal. Need aditional tool (e.g. Operator) to make it work |
| Cost | 1 instance + 100GB SSD storage cost $66.31/month | 1 instance + 100GB Zonal SSD PD cost $41.27/month  |


References:

https://cloud.google.com/blog/products/databases/to-run-or-not-to-run-a-database-on-kubernetes-what-to-consider
https://cloud.google.com/products/calculator#id=3018dbb0-8411-4e48-9dce-9670c31464a3
https://cloud.google.com/products/calculator#id=00a1b006-1856-4c96-b0a1-d002731b898f

### Exercise 3.07: Commitment

I'm using Postgres with PersistentVolumeClaims for this project because I have times for all the hurdles of learning and applying Kubernetes knowledge.

### Exercise 3.10

![](todo-log.png)
