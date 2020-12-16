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

Install argo-rollouts
```bash
kubectl create namespace argo-rollouts
kubectl apply -n argo-rollouts -f https://raw.githubusercontent.com/argoproj/argo-rollouts/stable/manifests/install.yaml
```

Create namespace
```bash
brew install kubectx # helper tool kubens
kubectl create namespace main-ns
kubectl create namespace todo-ns
kubens main-ns
```


### Exercise 4.03: Prometheus

Query:
```bash
scalar(count(kube_pod_info{namespace="prometheus", created_by_kind="StatefulSet"}))
```
