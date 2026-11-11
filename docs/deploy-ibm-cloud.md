# Deploy to IBM Cloud

These commands build and push the image to IBM Cloud Container Registry (ICR),
then create an application on IBM Cloud Code Engine. Install Docker and the IBM
Cloud CLI first, and ensure the account has access to the selected resource group,
registry, and Code Engine region.

## 1. Set deployment values and log in

Replace the example values. The API key should be kept in your shell environment
or secret manager, not committed to the repository.

```bash
export IBM_CLOUD_API_KEY="<api-key>"
export IBM_CLOUD_REGION="us-south"
export IBM_CLOUD_RESOURCE_GROUP="Default"
export REGISTRY_NAMESPACE="<unique-registry-namespace>"
export REGISTRY_HOST="us.icr.io"
export CE_PROJECT="tax-calculator-project"
export APP_NAME="tax-calculator"
export IMAGE_TAG="$(git rev-parse --short HEAD)"
export IMAGE="${REGISTRY_HOST}/${REGISTRY_NAMESPACE}/tax-calculator:${IMAGE_TAG}"

ibmcloud login --apikey "$IBM_CLOUD_API_KEY" \
  -r "$IBM_CLOUD_REGION" -g "$IBM_CLOUD_RESOURCE_GROUP"
ibmcloud plugin install container-registry -f
ibmcloud plugin install code-engine -f
ibmcloud cr region-set "$IBM_CLOUD_REGION"
```

Select the registry host for your IBM Cloud region (for example, `us.icr.io` for
US regions). Create a registry namespace once per account:

```bash
ibmcloud cr namespace-add "$REGISTRY_NAMESPACE"
ibmcloud cr login
```

## 2. Build and push the image

Run these commands from the repository root:

```bash
docker build -t "$IMAGE" .
docker push "$IMAGE"
ibmcloud cr image-list --restrict "$REGISTRY_NAMESPACE"
```

## 3. Create or select a Code Engine project

Create the project once. For later deployments, select the existing project.

```bash
ibmcloud ce project create --name "$CE_PROJECT" --region "$IBM_CLOUD_REGION"
ibmcloud ce project select --name "$CE_PROJECT"
```

## 4. Deploy the application

For the first deployment:

```bash
ibmcloud ce application create \
  --name "$APP_NAME" \
  --image "$IMAGE" \
  --port 8080 \
  --min-scale 1 \
  --max-scale 2
```

For later releases, update the existing application:

```bash
ibmcloud ce application update --name "$APP_NAME" --image "$IMAGE"
```

Retrieve the public URL from the application details:

```bash
ibmcloud ce application get --name "$APP_NAME"
```

Open the displayed `URL` and append `/health` to verify the service. Use the
`k8s/` manifests instead when deploying to IBM Cloud Kubernetes Service or
OpenShift; replace the image placeholder with the pushed image URI first.