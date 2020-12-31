Create cluster
```bash
k3d cluster create -p 8081:80@loadbalancer --agents 2
```

Install linkerd control plane resources
```bash
linkerd install | kubectl apply -f -
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
kubectl create namespace todo-ns
kubens todo-ns
```