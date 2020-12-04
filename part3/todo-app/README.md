```bash
docker build -t thangnv2212/todo-app . && docker push thangnv2212/todo-app

kubectl apply -f manifests/secret.yaml
kubectl apply -f manifests/statefulset.yaml
kubectl apply -f manifests/deployment.yaml
```

Go to localhost:8081/todos

![](todo.png)

### Exercise 3.10

![](todo-log.png)
