### Exercise 5.05: Deploy to Serverless

Install knative
https://knative.dev/docs/install/any-kubernetes-cluster/

```bash
docker build -t thangnv2212/pong-app . && docker push thangnv2212/pong-app

kubectl apply -k .
```

```
curl -H "Host: pong.main-ns.example.com" http://localhost:8081
```

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