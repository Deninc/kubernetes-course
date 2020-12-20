import kopf
import yaml
import pykube

@kopf.on.create('stable.dwk', 'v1', 'dummysites')
def create_fn(spec, **kwargs):
    url = spec["website_url"]
    name = kwargs["body"]["metadata"]["name"]
    doc = get_yaml(url, name)

    print(f"Serving html from: {url}")

    # Make it our child: assign the namespace, name, labels, owner references, etc.
    # When delete the custom resource, its children are also deleted.
    kopf.adopt(doc)

    api = pykube.HTTPClient(pykube.KubeConfig.from_env())
    dep = pykube.Deployment(api, doc)
    dep.create()
    api.session.close()

    return {'children': [dep.metadata['uid']]}


def get_yaml(url, name):
    return yaml.safe_load(f"""
        apiVersion: apps/v1
        kind: Deployment
        metadata:
          name: {name}-dep
        spec:
          replicas: 1
          selector:
            matchLabels:
              app: {name}
          template:
            metadata:
              labels:
                app: {name}
            spec:
              containers:
              - name: nginx
                image: nginx
                ports:
                - containerPort: 80
                volumeMounts:
                - name: workdir
                  mountPath: /usr/share/nginx/html
              initContainers:
              - name: init-html
                image: curlimages/curl:7.74.0
                command:
                - curl
                - '{url}'
                - -o
                - /work-dir/index.html
                volumeMounts:
                - name: workdir
                  mountPath: /work-dir
              dnsPolicy: Default
              volumes:
              - name: workdir
                emptyDir: {{}}
    """)
