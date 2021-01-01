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
