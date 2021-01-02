Create cluster
```bash
k3d cluster create --port '8082:30080@agent[0]' -p 8081:80@loadbalancer --agents 2 --k3s-server-arg '--no-deploy=traefik'
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
kubens todo-ns
```

### Exercise 5.03: Learn from external material

![""](flagger.png)
*Flagger automated canary releases*

### Exercise 5.04: Platform comparison

Comparing OpenShift vs Rancher, I'd choose Rancher because:
- Rancher use vanilla Kubernetes -> no vendor lock-in
- Rancher's tools are open-sourced -> +1 moral point
- Enterprise support is cheaper

References:
https://www.kloia.com/blog/openshift-vs-rancher
https://ubuntu.com/kubernetes/compare


### Exercise 5.06: Landscape

- Tools that I've used outside the course (in blue):
    - Databases: Hadoop, MongoDB, PostgreSQL, Redis
    - Messaging/Streaming: Kafka, Apache Spark
    - Docker related: Compose, Swarm, Amazon ECS & ECR
    - Monitoring: Amazon Cloudwatch, Zabbix, logstash, elastic
    - Deployment, CI/CD: Ansible, Heroku, Github Actions, Gitlab
- Tools that I've learned through the course (in green):
    - Kubernetes platform: k3s (local), GKE & Google Container Registry (cloud)
    - Monitoring: Prometheus, Grafana, Loki
    - Package manager: Helm (e.g. to install Prometheus)
    - Service mesh: Linkerd
    - Canary release: argo
    - Messaging/Streaming: NATS
    - Serverless: Knative

- Dependencies tools:
    - Distributed services coordination: etcd (for Kubernetes), Zookeeper (for Hadoop, Kafka)
    - Columnar data format: Avro (for Hadoop, Kafka)
    - Service proxy: Knative need Contour (Kubernetes ingress), which using Envoy (proxy). k3s use Traefik Proxy under the hood for ingress
    - Google Persistent Disk is used for GKE persistent volumes
    - Containerd is container runtime for Docker, Kubernetes (k3s)
    - OAuth2 is popular authentication tool used by many projects 
    - k3s also uses CoreDNS for DNS, and Flannel & gRPC for container networking

![](landscape.png)