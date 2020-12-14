Create cluster
```bash
k3d cluster create --port '8082:30080@agent[0]' -p 8081:80@loadbalancer --agents 2
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
