# Tekton alternative

The pipeline in `pipeline.yaml` runs clone, Flake8, pytest, image build/push, and
Code Engine deployment in order. It expects a Tekton installation and a cluster
that permits the Buildah task's privileged container. Use an isolated namespace
and follow your cluster's security policy before granting that permission.

Create a Docker configuration secret for IBM Container Registry and an IBM Cloud
API key secret. The `docker-registry-auth` secret must contain a `.dockerconfigjson`
key; `ibm-cloud-credentials` must contain an `apikey` key. For a private Git
repository, also configure the cluster's standard Tekton Git credentials.

Create a writable PVC named `tax-calculator-workspace`, or change the claim name
in the PipelineRun to one available in your cluster. Apply the task and pipeline
definitions, then start a run:

```bash
kubectl apply -f tasks.yaml
kubectl apply -f pipeline.yaml
kubectl apply -f pipelinerun.yaml
```

Edit `pipelinerun.yaml` with the repository URL, image URI, IBM Cloud region,
resource group, and existing Code Engine project. `REGISTRY_HOST` and namespace
in the image URI must correspond to the IBM Cloud account and region.