# User Stories

## 1. Containerize the application

As a developer, I want the Tax Calculator packaged in a small, non-root Docker
image, so that it runs consistently across local and cloud environments.

- Acceptance criteria: The image uses Python 3.11 slim, runs as a non-root user,
  exposes port 8080, serves the app with Gunicorn, and has a health check.
- Story points: 3

## 2. Deploy to IBM Cloud

As a platform engineer, I want to deploy the image to IBM Cloud Code Engine, so
that users can access the calculator through a public application URL.

- Acceptance criteria: The image is pushed to IBM Cloud Container Registry; a
  Code Engine application listens on port 8080; deployment instructions explain
  how to retrieve its public URL.
- Story points: 5

## 3. Add a CI pipeline

As a developer, I want pushes and pull requests to `main` to trigger CI, so that
code changes receive consistent automated checks.

- Acceptance criteria: GitHub Actions checks out the source, sets up Python 3.11,
  installs dependencies, runs Flake8 and pytest with coverage, and builds Docker.
- Story points: 5

## 4. Run unit tests in the pipeline

As a maintainer, I want the tax calculation and web routes tested in CI, so that
regressions in calculations and input validation are caught before merge.

- Acceptance criteria: Tests cover each filing-status bracket boundary, zero and
  invalid income, invalid status, the home and health routes, the JSON API, and
  HTTP 400 responses for invalid inputs.
- Story points: 3

## 5. Automate deployment

As a release engineer, I want successful CI runs on `main` to publish and deploy
the matching image, so that releases do not depend on manual deployment steps.

- Acceptance criteria: CD runs only after successful CI on `main`, authenticates
  with GitHub secrets, pushes a commit-tagged image, and creates or updates the
  Code Engine application.
- Story points: 8

## 6. Provide a Kubernetes alternative

As a cluster operator, I want Kubernetes deployment and service manifests, so
that I can run the app on IBM Cloud Kubernetes or OpenShift instead.

- Acceptance criteria: Manifests include a Deployment with health probes and a
  Service that can expose the application on port 8080.
- Story points: 3